import unittest 
from flask import url_for
from flask_testing import TestCase
from application import app, db, routes, forms 
from application.models import maps, regions


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///")
        app.config['SECRET_KEY'] = '321hut234987fh2934n9fg132w489tgyh'
        return app

    def setUp(self):
        db.create_all()
        new_vastir = regions(id=7, name="New_Vastir")
        db.session.add
        db.session.commit()
        map1 = maps(id=1, regions_id=7, name="test", base_tier=1, max_tier=16, Layout="A", boss=2) 

        db.session.add(map1)
        db.session.commit()
    
    def tearDown(self):
        db.drop_all()



class Test_Home_Page(TestBase):
    def test_home_html(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
        

class Test_Update_Page(TestBase):
    def test_update_html(self):
        response = self.client.get("/update/1")
        self.assertEqual(response.status_code, 200 )

    def test_get_form(self):
        response = self.client.get("update/1")
        self.assertIn(b"1", response.data)

    def test_get_form2(self):
        response = self.client.get("update/1")
        self.assertIn(b"test", response.data)
    
    def test_get_form3(self):
        response = self.client.get("update/1")
        self.assertIn(b"16", response.data)

    def test_get_form4(self):
        response = self.client.get("update/1")
        self.assertIn(b"A", response.data)

    def test_get_form5(self):
        response = self.client.get("update/1")
        self.assertIn(b"2", response.data)

    
class Test_Delete_Page(TestBase):
    def test_delete_html(self):
        response = self.client.post("delete/1")
        self.assertEqual(response.status_code, 302)
    

class Test_New_Vastir_Page(TestBase):
    def test_vastir_html(self):
        response = self.client.get(url_for("New_Vastir"))
        self.assertEqual(response.status_code, 200)
    
    def test_find_map1(self):
        response = self.client.get(url_for("New_Vastir"))
        self.assertIn(b"test", response.data)


class Test_New_Vastir_Tree_Page(TestBase):
    def test_vastir_tree_html(self):
        response = self.client.get(url_for("New_Vastir_Tree"))
        self.assertEqual(response.status_code, 200)       
       
       
       
class Test_Lex_Ejoris_Page(TestBase):
    def test_lex_ejoris_html(self):
        response = self.client.get(url_for("Lex_Ejoris"))
        self.assertEqual(response.status_code, 200)
       
       
class Test_Lex_Ejoris_Tree_Page(TestBase):
    def test_lex_ejoris_tree_html(self):
        response = self.client.get(url_for("Lex_Ejoris_Tree"))
        self.assertEqual(response.status_code, 200)


class Test_Tirns_Page(TestBase):
    def test_tirns_end_html(self):
        response = self.client.get(url_for("Tirns_End"))
        self.assertEqual(response.status_code, 200)


class Test_Tirns_Tree_Page(TestBase):
    def test_tirns_end_tree_html(self):
        response = self.client.get(url_for("Tirns_End_Tree"))
        self.assertEqual(response.status_code, 200)


class Lex_Proxima_Page(TestBase):
    def test_lex_proxima_html(self):
        response = self.client.get(url_for("Lex_Proxima"))
        self.assertEqual(response.status_code, 200)

class Test_Lex_Proxima_Tree_Page(TestBase):
    def test_lex_proxima_tree_html(self):
        response = self.client.get(url_for("Lex_Proxima_Tree"))
        self.assertEqual(response.status_code, 200)


class Glennach_Cairns_Page(TestBase):
    def test_glennach_cairns_html(self):
        response = self.client.get(url_for("Glennach_Cairns"))
        self.assertEqual(response.status_code, 200)

class Glennach_Cairns_Tree_Page(TestBase):
    def test_glennach_cairns_tree_html(self):
        response = self.client.get(url_for("Glennach_Cairns_Tree"))
        self.assertEqual(response.status_code, 200)


class Lira_Arthain_Page(TestBase):
    def test_lira_arthain_html(self):
        response = self.client.get(url_for("Lira_Arthain"))
        self.assertEqual(response.status_code, 200)


class Lira_Arthain_Tree_Page(TestBase):
    def test_lira_arthain_tree_html(self):
        response = self.client.get(url_for("Lira_Arthain_Tree"))
        self.assertEqual(response.status_code, 200)


class Haewark_Hamlet_Page(TestBase):
    def test_haewark_hamlet_html(self):
        response = self.client.get(url_for("Haewark_Hamlet"))
        self.assertEqual(response.status_code, 200)


class Valdos_Rest_Page(TestBase):
    def test_valdos_rest_html(self):
        response = self.client.get(url_for("Valdos_Rest"))
        self.assertEqual(response.status_code, 200)


class Valdos_Rest_Tree_Page(TestBase):
    def test_valdos_rest_tree_html(self):
        response = self.client.get(url_for("Valdos_Rest_Tree"))
        self.assertEqual(response.status_code, 200)


class Uncharted_Realms_Page(TestBase):
    def uncharted_realms_html(self):
        response = self.client.get(url_for("Uncharted_Realms"))
        self.assertEqual(response.status_code, 200)


class Divination_Cards_Page(TestBase):
    def divination_cards_html(self):
        response = self.client.get(url_for("Divination_Cards"))
        self.assertEqual(response.status_code, 200)










