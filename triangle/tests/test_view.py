from django.test import TestCase

class TriangleViewsTestCase(TestCase):
    def test_index(self):
        response=self.client.get('/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("We Are Creative Nerds",decode_content)
        self.assertIn("Triangle Corporate Template",decode_content)
        self.assertIn("Experienced and Enthusiastic",decode_content)
        self.assertIn("Testimonial",decode_content)
        self.assertIn("Contacts",decode_content)
        self.assertIn("Your Company 2014. All Rights Reserved.",decode_content)
        self.assertIn("Send a message",decode_content)

    
    def test_add_response(self):
        response=self.client.get('/add-response/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("our text here:",decode_content)

    def test_about(self):
        response=self.client.get('/about/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("About Us",decode_content)
        self.assertIn("Triangle Corporate Template",decode_content)
        self.assertIn("Meet the Team",decode_content)
        self.assertIn("Testimonial",decode_content)
        self.assertIn("Contacts",decode_content)
        self.assertIn("Send a message",decode_content)

    def test_services(self):
        response=self.client.get('/services/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Services",decode_content)
        self.assertIn("Why Choose Us?",decode_content)
        self.assertIn("Triangle Corporate Template",decode_content)
        self.assertIn("Recent Projects",decode_content)
        self.assertIn("Happy Clients",decode_content)
        self.assertIn("Testimonial",decode_content)
        self.assertIn("Contacts",decode_content)
        self.assertIn("Send a message",decode_content)

    def test_pricing(self):
        response=self.client.get('/pricing/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Pricing",decode_content)
        self.assertIn("Testimonial",decode_content)
        self.assertIn("Contacts",decode_content)
        self.assertIn("Send a message",decode_content)
        
    def test_contacts(self):
        response=self.client.get('/contacts/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Contact Us",decode_content)
        self.assertIn("Testimonial",decode_content)
        self.assertIn("Contacts",decode_content)
        self.assertIn("Send a message",decode_content)

    def test_blog(self):
        response=self.client.get('/blog/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Blog",response.content.decode())
        self.assertIn("All Posts",decode_content)        
        self.assertIn("Tag Cloud",decode_content)   
        self.assertIn("Testimonial",decode_content)
        self.assertIn("Contacts",decode_content)
        self.assertIn("Send a message",decode_content)

    # def test_blog_slug(self):
    #     response=self.client.get('/blog/advanced_business_cards_design_1/')
    #     decode_content=response.content.decode()

    #     self.assertEqual(response.status_code,200)
    #     self.assertIn("Blog",decode_content)
    #     self.assertIn("Categories",decode_content)
    #     self.assertIn("Tag Cloud",decode_content)
    #     self.assertIn("Advanced business cards design",decode_content)
    #     self.assertIn("Comments",decode_content)
    #     self.assertIn("Testimonial",decode_content)
    #     self.assertIn("Contacts",decode_content)
    #     self.assertIn("Send a message",decode_content)

    def test_add_comment(self):
        response=self.client.get('/add-comment/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Your text here:",decode_content)

    # def test_portfolio(self):
    #     response=self.client.get('/portfolio')

    #     decode_content=response.content.decode()

    #     self.assertEqual(response.status_code,301)
    #     self.assertIn("Portfolio",decode_content)
    #     self.assertIn("Testimonial",decode_content)
    #     self.assertIn("Contacts",decode_content)
    #     self.assertIn("Send a message",decode_content)

    def test_portfolio_slug(self):
        response=self.client.get('/portfolio/sailing_vivamus')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Portfolio",decode_content)
        self.assertIn("Skills:",decode_content)
        self.assertIn("Client:",decode_content)
        self.assertIn("Related Work",decode_content)
        self.assertIn("Testimonial",decode_content)
        self.assertIn("Contacts",decode_content)
        self.assertIn("Send a message",decode_content)

    def test_login(self):
        response=self.client.get('/login/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Email:",decode_content)
        self.assertIn("Password:",decode_content)
        self.assertIn("Captcha:",decode_content)

    def test_add_user(self):
        response=self.client.get('/add-user/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Your Name:",decode_content)
        self.assertIn("Your E-mail:",decode_content)
        self.assertIn("Add your small photo:",decode_content)
        self.assertIn("Add your big photo:",decode_content)
        self.assertIn("Your password:",decode_content)
        self.assertIn("Replay Your password:",decode_content)
        self.assertIn("Captcha:",decode_content)


    def test_logout(self):
        response=self.client.get('/logout/')

        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,'/')

    def test_order(self):
        response=self.client.get('/order/')
        decode_content=response.content.decode()

        self.assertEqual(response.status_code,200)
        self.assertIn("Your pricing:",decode_content)
        self.assertIn("Your text here:",decode_content)