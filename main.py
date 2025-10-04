from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager,  Screen
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.popup import Popup
from kivy.core.window import Window

Builder.load_string("""
#: import utils kivy.utils

<Loginwindow>:
	canvas.before:
		Color:
			rgb: 10/255.0 ,7/255.0,71/255.0
		Rectangle:
			pos: self.pos
			size: self.size 
	FloatLayout:
		Label:
			text: "Email :"
			pos_hint: {"x": -0.2 , "y":0.4}
			font_size: "25sp"
			
		TextInput:
			id: email
			multiline: False
			size_hint: .3 , .05
			pos_hint: {"x": 0.5 , "y":0.87}
			font_size: "15sp"
			background_color: "gray"
			
		Label:
			text: "Password :"
			pos_hint: {"x": -0.2 , "y":0.3}
			font_size: "25sp"
			
		TextInput:
			id: password
			multiline: False
			size_hint: .3 , .05
			password: True
			pos_hint: {"x": 0.5 , "y":0.77}
			font_size: "15sp"
			background_color: "gray"
			
		Button:
			text: "Don't have any , Create one"
			size_hint: .5 , .1
			font_size: "15sp"
			pos_hint: {"x": 0.25, "y": 0.32}
			background_color: "darkblue"
			on_release:
				root.manager.current = "create_account"
				root.manager.transition.direction = "right"
				
		Button:
			text: "Log In"
			size_hint: 0.6, 0.1
			font_size: "20sp"
			pos_hint: {"x":0.2 , "y":0.2}
			background_normal: ""
			background_color: utils.get_color_from_hex("#4681f4")
			on_release: root.login()


<Create_account_window>:
	canvas.before:
		Color:
			rgb: 10/255.0 , 7/255.0, 71/255.0
		Rectangle:
			pos: self.pos
			size: self.size
	FloatLayout:
		Label:
			text: "Name :"
			font_size: "20sp"
			pos_hint: {"x": -0.2, "y":0.4}
			
		TextInput:
			id: name_input
			multiline: False 
			pos_hint: {"x": 0.5, "y":0.87}
			size_hint: .3, .05
			font_size: "15sp"
			background_color: "gray"
			
		Label:
			text: "Email :"
			pos_hint: {"x":-0.2, "y": 0.3}
			font_size: "20sp"
			
		TextInput:
			id: email_input
			multiline: False 
			pos_hint: {"x": 0.5, "y":0.77}
			size_hint: .3, .05
			font_size: "15sp"
			background_color: "gray"
			
		Label:
			text: "Password :"
			font_size: "20sp"
			pos_hint: {"x": -0.2 , "y": 0.2}
			
		TextInput:
			id: password_input
			multiline: False 
			pos_hint: {"x": 0.5, "y":0.67}
			size_hint: .3, .05
			font_size: "15sp"
			background_color: "gray"
			
		Button:
			text: "Create account"
			font_size: "30sp"
			size_hint: .6 , .1
			pos_hint: {"x": 0.2, "y": 0.3}
			background_color: "darkblue"
			on_release:
				root.save_data()
		
		Button:
			text: "Go Back"
			font_size: "20sp"
			size_hint: 0.4, 0.05
			pos_hint: {"x": 0.3, "y": 0.2}
			background_color: "darkblue"
			on_release:
				root.manager.current = "loginscreen"
				root.manager.transition.direction = "left"

<Create_account_window_popup>:
	FloatLayout:
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		Label:
			text: "Please enter all information"
			pos_hint: {"center_x": 0.5, "center_y": .5}
			font_size: "15sp"
			
<Invalid_password_popup>:
	FloatLayout:
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		Label:
			text: "Wrong Password"
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			font_size: "15sp"

<Invalid_email_popup>:
	FloatLayout:
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		Label:
			text: "Wrong Email"
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			font_size: "15sp"

<Invalid_input_popup>:
	FloatLayout:
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		Label:
			text: "Check Everything loser"
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			font_size: "15sp"

<No_account_popup>:
	FloatLayout:
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		Label:
			text: "You don't have any account"
			pos_hint: {"center_x": 0.5, "center_y": 0.5}
			font_size: "15sp"

<Mainwindow>:
	canvas.before:
		Color:
			rgb: 10/255.0 ,7/255.0,71/255.0
		Rectangle:
			pos: self.pos
			size: self.size
	FloatLayout:
		Label:
			text: "You logged in successfully"
			font_size: "30sp"
			pos_hint: {"center_x": 0.5, "center_y": 0.6}
					
		Button:
			text: "Go back"
			font_size: "20sp"
			pos_hint: {"center_x": 0.5, "center_y": 0.45}
			size_hint: 0.4, 0.06
			background_color: "darkblue"
			on_release:
				root.manager.current = "loginscreen"
				root.manager.transition.direction = "right"
""")


class Loginwindow(Screen):
	
	def login(self):
		email = self.ids.email.text
		password = self.ids.password.text
		
		try:
			with open("data.txt") as f:
				self.check_data = f.read()
				self.check_data = self.check_data.split(",")
			
				if email == self.check_data[1] and password == self.check_data[2]:
					sm.current = "main"
					sm.transition.direction = "left"
					self.ids.email.text = ""
					self.ids.password.text = ""
				
				elif email != self.check_data[1] and password == self.check_data[2] and email != "":
					Invalid_email()
				
				elif password != self.check_data[2] and email == self.check_data[1] and password != "":
					Invalid_password()
				
				elif email == "" and password == "":
					show_popup_at_create_account_window()
				
				elif email == email and password == "" :
					show_popup_at_create_account_window()
				
				elif email == "" and password == password:
					show_popup_at_create_account_window()
				
				else:
					Invalid_input()
					
		except FileNotFoundError:
				no_account()
				

class Invalid_password_popup(FloatLayout):
	pass
	
class Invalid_email_popup(FloatLayout):
	pass

class Invalid_input_popup(FloatLayout):
	pass

class No_account_popup(FloatLayout):
	pass

class Create_account_window(Screen):
	
	def save_data(self):
		name = self.ids.name_input.text
		email = self.ids.email_input.text
		password = self.ids.password_input.text
		
		if name == "" or email == "" or password == "":
			show_popup_at_create_account_window()
		
		else:
			with open("data.txt" , "w") as f:
				self.data = f"{name},{email},{password}"
				f.write(self.data)
		
			sm.current = "loginscreen"
			sm.transition.direction = "left"
			
			self.ids.name_input.text = ""
			self.ids.email_input.text = ""
			self.ids.password_input.text = ""
		
class Create_account_window_popup(FloatLayout):
	pass
	
	
class Mainwindow(Screen):
	pass
	

sm = ScreenManager()
sm.add_widget(Loginwindow(name = "loginscreen"))
sm.add_widget(Create_account_window(name = "create_account"))
sm.add_widget(Mainwindow(name = "main"))
#sm.current = "create_account"

#--------------------------------------------------------------------------------------
class MyApp(App):
	def build(self):
		Window.size = (400, 650)
		return sm
#------------------‐-------------------------------------------------------------------


def show_popup_at_create_account_window():
	msg = Create_account_window_popup()
	
	popupwindow = Popup(title="Important message", content=msg , size_hint=(None , None), size=(300, 400))
	popupwindow.open()
	

def Invalid_password():
	info = Invalid_password_popup()
	popup_1 = Popup(title="info", content=info, size_hint=(None,None), size=(300, 400))
	popup_1.open()
	
	
def Invalid_email():
	info = Invalid_email_popup()
	popup_2 = Popup(title="info" , content=info , size_hint=(None,None), size=(300, 400))
	popup_2.open()
	

def Invalid_input():
	msg = Invalid_input_popup()
	popup_3 = Popup(title="info", content=msg, size_hint=(None, None), size=(300, 400))
	popup_3.open()


def no_account():
	info = No_account_popup()
	popup_4 = Popup(title="info", content=info, size_hint=(None,None), size=(300, 400))
	popup_4.open()


MyApp().run()