from flask import Flask, render_template, redirect, url_for, request
from application import app, db
from application.models import regions, bases, maps, cards, cmap 
from application.forms import Map_Create_Form
import os

picFolder = os.path.join("static","pics")
app.config["UPLOAD_FOLDER"] = picFolder
app.config['SECRET_KEY'] = 'fu32nh3u224nfu23nognowdqong23go'


@app.route("/")
def home():
    atlas = os.path.join(app.config["UPLOAD_FOLDER"],"atlas.png")
    title = os.path.join(app.config["UPLOAD_FOLDER"],"atlas_title.png")
    div = os.path.join(app.config["UPLOAD_FOLDER"], "div_card.png")
    
    
    return render_template("home.html",
    home_image = atlas,
    title_image= title,
    div_card_icon = div)





@app.route("/New Vastir", methods = ["Get", "POST"])
def New_Vastir():
    Vastir = os.path.join(app.config["UPLOAD_FOLDER"], "New_Vastir_Tree.png")
    Vastir_Title = os.path.join(app.config["UPLOAD_FOLDER"], "New_Vastir_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")
    form = Map_Create_Form()
    if form.validate_on_submit():
        new_map = maps( 
        regions_id=form.regions_id.data,        
        name=form.name.data,
        base_tier=form.base_tier.data,
        max_tier=form.max_tier.data,
        Layout=form.Layout.data,
        boss=form.boss.data) 
        
        db.session.add(new_map)
        db.session.commit()
        return redirect(url_for("home"))

    
    return render_template("New_Vastir.html",
    NV_image = Vastir,
    NV_Title = Vastir_Title,
    HomeB = Button,
    form = form)





@app.route("/New Vastir Skill Tree")
def New_Vastir_Tree():
    NVTree = os.path.join(app.config["UPLOAD_FOLDER"], "New_Vastir_Tree.png")
    return render_template("New_Vastir_Tree.html", NV_image =  NVTree)





@app.route("/Lex Ejoris")
def Lex_Ejoris():
    Ejoris = os.path.join(app.config["UPLOAD_FOLDER"], "Lex_Ejoris_Tree.png")
    Ejoris_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Lex_Ejoris_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")
    

    return render_template("Lex_Ejoris.html",
    LE_image = Ejoris,
    LE_Title = Ejoris_Title,
    HomeB = Button)





@app.route("/Lex Ejoris Skill Tree")
def Lex_Ejoris_Tree():
    LETree = os.path.join(app.config["UPLOAD_FOLDER"], "Lex_Ejoris_Tree.png")
    return render_template("Lex_Ejoris_Tree.html", LE_image = LETree, headings=headings, data=data)





@app.route("/Tirn's End")
def Tirns_End():
    End = os.path.join(app.config["UPLOAD_FOLDER"], "Tirns_End_Tree.png")
    End_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Tirns_End_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Tirns_End.html",
    TE_image = End,
    TE_Title = End_Title,
    HomeB = Button)





@app.route("/Tirn's End Skill Tree")
def Tirns_End_Tree():
    TETree = os.path.join(app.config["UPLOAD_FOLDER"], "Tirns_End_Tree.png")
    return render_template("Tirns_End_Tree.html", TE_image = TETree)





@app.route("/Lex Proxima")
def Lex_Proxima():
    Proxima = os.path.join(app.config["UPLOAD_FOLDER"], "Lex_Proxima_Tree.png")
    Proxima_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Lex_Proxima_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Lex_Proxima.html",
    LP_image = Proxima,
    LP_Title = Proxima_Title,
    HomeB = Button)




    
@app.route("/Lex Proxima Skill Tree")
def Lex_Proxima_Tree():
    LPTree = os.path.join(app.config["UPLOAD_FOLDER"], "Lex_Proxima_Tree.png")
    return render_template("Lex_Proxima_Tree.html", LP_image = LPTree)





@app.route("/Glennach Cairns")
def Glennach_Cairns():
    Cairns = os.path.join(app.config["UPLOAD_FOLDER"], "Glennach_Cairns_Tree.png")
    Cairns_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Glennach_Cairns_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Glennach_Cairns.html",
    GC_image = Cairns,
    GC_Title = Cairns_Title,
    HomeB = Button)





@app.route("/Glennach Cairns Skill Tree")
def Glennach_Cairns_Tree():
    GCTree = os.path.join(app.config["UPLOAD_FOLDER"], "Glennach_Cairns_Tree.png")
    return render_template("Glennach_Cairns_Tree.html", GC_image = GCTree)





@app.route("/Lira Arthain")
def Lira_Arthain():
    Arthain = os.path.join(app.config["UPLOAD_FOLDER"], "Lira_Arthain_tree.png")
    Arthain_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Lira_Arthain_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Lira_Arthain.html",
    LA_image = Arthain,
    LA_Title = Arthain_Title,
    HomeB = Button)





@app.route("/Lira Arthain Skill Tree")
def Lira_Arthain_Tree():
    LATree = os.path.join(app.config["UPLOAD_FOLDER"], "Lira_Arthain_tree.png")
    return render_template("Lira_Arthain_Tree.html", LA_image =LATree)





@app.route("/Haewark Hamlet")
def Haewark_Hamlet():
    Hamlet = os.path.join(app.config["UPLOAD_FOLDER"], "Haewark_Hamlet_Tree.png")
    Hamlet_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Haewark_Hamlet_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Haewark_Hamlet.html",
    HH_image = Hamlet,
    HH_Title = Hamlet_Title,
    HomeB = Button)





@app.route("/Haewark Hamlet Skill Tree")
def Haewark_Hamlet_Tree():
    HHTree = os.path.join(app.config["UPLOAD_FOLDER"], "Haewark_Hamlet_Tree.png")
    return render_template("Haewark_Hamlet_Tree.html", HH_image = HHTree)





@app.route("/Valdo's Rest")
def Valdos_Rest():
    Rest = os.path.join(app.config["UPLOAD_FOLDER"], "Valdos_Rest_Tree.png")
    Rest_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Valdos_Rest_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Valdos_Rest.html",
    VR_image = Rest,
    VR_Title = Rest_Title,
    HomeB = Button)





@app.route("/Valdo's Rest Skill Tree")
def Valdos_Rest_Tree():
    VRTree = os.path.join(app.config["UPLOAD_FOLDER"], "Valdos_Rest_Tree.png")
    return render_template("Valdos_Rest_Tree.html", VR_image = VRTree)  





@app.route("/Uncharted Realms")
def Uncharted_Realms():
    Realms = os.path.join(app.config["UPLOAD_FOLDER"], "Uncharted_Realms_Tree.png")
    Realms_Title = os.path.join(app.config["UPLOAD_FOLDER"], "Realms_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Uncharted_Realms.html",
    UR_image = Realms,
    UR_Title = Realms_Title,
    HomeB = Button)





@app.route("/Divination Cards")
def Divination_Cards():
    Card_Title= os.path.join(app.config["UPLOAD_FOLDER"], "Card_Title.png")
    Button = os.path.join(app.config["UPLOAD_FOLDER"], "Home_Button.png")


    return render_template("Divination_Cards.html",
    DC_image = Card_Title,
    HomeB = Button)




