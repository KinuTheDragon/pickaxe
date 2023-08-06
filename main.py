from flask import Flask, render_template, abort, request, redirect, make_response, url_for, jsonify
from load import blocks, items, enchants, communist_items, artifacts
from block import Block
from item import Item
from enchantment import Enchantment
from constants import ACHIEVEMENTS, MEDALS
from flask.app import HTTPException
from jwt_util import create_jwt_token, verify_jwt_token
import re, hashlib, hmac, os, sys

is_dev_version = "REPL_ID" in os.environ

if not is_dev_version:
    from dotenv import load_dotenv
    load_dotenv()

def verify_signature(payload_body, secret_token, signature_header):
    """Verify that the payload was sent from GitHub by validating SHA256.

    Raise and return 403 if not authorized.

    Args:
        payload_body: original request body to verify (request.body())
        secret_token: GitHub app webhook token (WEBHOOK_SECRET)
        signature_header: header received from GitHub (x-hub-signature-256)
    """
    if not signature_header:
        raise HTTPException(status_code=403, detail="x-hub-signature-256 header is missing!")
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    if not hmac.compare_digest(expected_signature, signature_header):
        raise HTTPException(status_code=403, detail="Request signatures didn't match!")

app = Flask(__name__)

def is_admin():
    token = request.cookies.get("token")
    verified = verify_jwt_token(token)
    return verified

@app.post("/api/webhook")
def github_webhook():
    data = request.get_data()
    verify_signature(data,
        os.environ["github_secret"],
        request.headers.get("x-hub-signature-256"))

    os.system("git reset --hard && git pull")
    os._exit(0)

@app.route("/")
def index():
    return render_template("index.html",
                           msg = request.args.get("msg"),
                           is_dev_version = is_dev_version,
                           admin = is_admin)

@app.route("/block/<href>")
def block(href):
    for b in blocks.values():
        if b.href == f"/block/{href}":
            return render_template("block.html", block = b)
    return abort(404)

@app.route("/json/block/<href>")
def block_json(href):
    for b in blocks.values():
        if b.href == f"/block/{href}":
            return b.json()
    return abort(404)

LINK_REGEX = re.compile(r"\[([^\]]+)\]")

@app.route("/item/<href>")
def item(href):
    for i in items.values():
        if i.href == f"/item/{href}":
            def get_block_item(name):
                block_matches = [b for b in Block.all_blocks if b.name == name]
                item_matches = [i for i in Item.all_items if i.name == name]
                enchantment_matches = [e for e in Enchantment.all_enchantments if e.name == name]
                matches = block_matches + item_matches + enchantment_matches
                assert len(matches) == 1, f"{len(matches)} matches found for {name}"
                return matches[0]
            def get_links(text):
                return LINK_REGEX.sub(
                    lambda m: get_block_item(m.group(1))
                        .icon(url_for),
                    text
                )
            return render_template("item.html", item = i,
                                   get_links = get_links,
                                   Item = Item,
                                   reqhat = isinstance(
                                       i.crafting_tier.value, tuple
                                   ) if i.crafting_tier else None)
    return abort(404)

@app.route("/json/item/<href>")
def item_json(href):
    for i in items.values():
        if i.href == f"/item/{href}":
            return i.json()
    return abort(404)

@app.route("/enchant/<href>")
def enchant(href):
    for e in enchants.values():
        if e.href == f"/enchant/{href}":
            return render_template("enchant.html", enchant = e,
                                   enumerate = enumerate)
    return abort(404)

@app.route("/json/enchant/<href>")
def enchant_json(href):
    for e in enchants.values():
        if e.href == f"/enchant/{href}":
            return e.json()
    return abort(404)

@app.route("/artifact/<href>")
def artifact(href):
    for a in artifacts.values():
        if a.href == f"/artifact/{href}":
            return render_template("artifact.html", artifact = a)
    return abort(404)

@app.route("/json/artifact/<href>")
def artifact_json(href):
    for a in artifacts.values():
        if a.href == f"/artifact/{href}":
            return a.json()
    return abort(404)

def sort_key(x, get_name = True):
    name = x.name.lower() if get_name else x.lower()
    while not name[0].isalnum(): name = name[1:]
    if name.startswith("the "): name = name[4:]
    return name

@app.route("/blocks")
def blocklist():
    block_list = sorted(list(blocks.values()),
                        key = sort_key)
    return render_template("blocklist.html",
                           blocks = block_list)

@app.route("/items")
def itemlist():
    item_list = sorted(list(items.values()),
                        key = sort_key)
    return render_template("itemlist.html",
                           items = item_list)

@app.route("/json/items")
def itemlist_json():
    item_list = sorted(list(items.values()), key = sort_key)
    return [
        {
            "name": item.name,
            "id": item.item_id,
            "enchanted": item.item_enchanted,
            "rarity": item.rarity.value,
            "path": item.href,
            "lore": item.lore
        }
        for item in item_list
    ]

@app.route("/enchants")
def enchlist():
    ench_list = sorted(list(enchants.values()),
                        key = sort_key)
    return render_template("enchantlist.html",
                           enchants = ench_list)

@app.route("/artifacts")
def artilist():
    arti_list = sorted(list(artifacts.values()),
                        key = lambda a: a.number)
    return render_template("artifactlist.html",
                           artifacts = arti_list)

@app.route("/communist")
def communist():
    return render_template("communist.html", items = communist_items)

@app.route("/museum")
def museum():
    museumables = [item for item in items.values() if item.museum_position]
    arrayed = []
    for item in museumables:
        page, row, col = [i - 1 for i in item.museum_position]
        while page >= len(arrayed):
            arrayed.append([[None] * 9 for i in range(4)])
        arrayed[page][row][col] = item
    return render_template("museum.html",
                           items = arrayed,
                           enumerate = enumerate)

@app.route("/settings")
def settings():
    return render_template("settings.html",
                           settings = request.cookies)

@app.route("/updatesettings", methods = ["POST"])
def update_settings():
    response = make_response(redirect("/?msg=updated"))
    response.set_cookie("sporetex", b"1" * ("tex" in request.form))
    return response

@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/search")
def search():
    links = sorted(list({
        (x.name, x.icon(url_for).replace('"', '\\"')) for x in
        list(blocks.values()) +
        list(items.values()) +
        list(enchants.values()) +
        list(artifacts.values())
    }), key = lambda i: sort_key(i[0], False))
    return render_template("search.html",
                           links = links)

@app.route("/sputtrooms")
def sputtrooms():
    return render_template("sputtrooms.html")

@app.route("/suggest")
def suggest():
    return render_template("suggest.html",
                           error = request.args.get("error"))

@app.route("/submitsuggest", methods = ["POST"])
def submit_suggest():
    try:
        suggestion, name = request.form["suggestion"], request.form["name"]
        assert suggestion and name
    except (KeyError, AssertionError):
        return redirect("/suggest?error=1")
    with open("suggestions.txt", "a") as f:
        replaced = suggestion.replace("\n", "\n    ")
        f.write(f"From {name}:\n    {replaced}\n")
    return redirect("/?msg=submit")

@app.route("/progression")
def progression():
    return render_template("progression.html", Block = Block, Item = Item)

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html", achievements = ACHIEVEMENTS)

@app.route("/medals")
def medals():
    return render_template("medals.html", medals = MEDALS, len = len)

@app.route("/admin")
def admin():
    if is_admin():
        response = make_response(redirect("/?msg=unadmin"))
        response.set_cookie("token", "", expires = 0)
        return response
    return render_template("admin.html",
                           error = request.args.get("error"))

@app.route("/enableadmin", methods = ["POST"])
def enable_admin():
    passhash = request.form.get("passhash")
    if not isinstance(passhash, str):
        return redirect("/admin?error=invalid")
    double_hash = hashlib.sha512(passhash.encode()).hexdigest()
    if double_hash != "37272436e6d46402d8525b52b65e49ab664af82e97f6ce560d328f006da72071fef9494e95bc168dece19898ca8489c9ce0374c785022e798a4415a1bd8677ec":
        return redirect("/admin?error=wrong")
    response = make_response(redirect("/?msg=admin"))
    response.set_cookie("token",
                        create_jwt_token({"admin": True}).encode())
    return response

@app.route("/suggestions")
def suggestion_list():
    if not is_admin():
        return redirect("/?msg=noadmin")
    with open("suggestions.txt") as f:
        suggestions = f.read()
    return render_template("suggestion_list.html",
                           suggestions = suggestions)

@app.route("/updatesuggests", methods = ["POST"])
def update_suggests():
    if not is_admin():
        return redirect("/?msg=noadmin")
    with open("suggestions.txt", "w") as f:
        f.write(request.form["suggests"])
    return redirect("/suggestions")

app.run(host = "0.0.0.0", port = 8080)