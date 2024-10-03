# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits


class Result(Screen):
     def __init__(self,**kwargs):
        super().__init__(**kwargs)

        outer = BoxLayout(orientation = 'vertical', padding = 8,spacing =8)
        instr = Label(text = 'place for result')

        outer.add_widget(instr)
        self.add_widget(outer)



class PulseScr2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        outer = BoxLayout(orientation = 'vertical', padding = 8,spacing =8)
        line1 = BoxLayout(size_hint=(0.8,None), height = '30sp')
        line2 = BoxLayout(size_hint =(0.8,None), height = '30sp')

        instr = Label(text=txt_test3)
        lbl1 = Label(text = 'Результат')
        self.in_result1 = TextInput(text='0', multiline=False)
        lbl2 = Label(text = 'Результат після відпочинку')
        self.in_result2 = TextInput(text='0', multiline=False)
        self.btn = Button(
            text = "Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        line1.add_widget(lbl1)
        line1.add_widget(self.in_result1)

        line2.add_widget(lbl2)
        line2.add_widget(self.in_result2)

        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        self.manager.current = 'result'


class CheckSits(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        outer = BoxLayout(orientation = 'vertical', padding = 8,spacing =8)
        

        instr = Label(text=txt_sits)
        self.btn = Button(
            text = "Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        outer.add_widget(instr)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        self.manager.current = 'pulse2'



class PulseScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        outer = BoxLayout(orientation = 'vertical', padding = 8,spacing =8)
        line = BoxLayout(size_hint=(0.8,None), height = '30sp')
        
        instr = Label(text=txt_test1)
        lbl_result = Label(text = "Введіть результат:")
        self.in_result = TextInput(text = '0', multiline = False)
        self.btn = Button(
            text = "Продовжити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)

        self.add_widget(outer)
        
    def next(self):
        self.manager.current = 'sits'



class InstScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        outer = BoxLayout(orientation = 'vertical', padding = 8,spacing =8)
        line1 = BoxLayout(size_hint=(0.8,None), height = '30sp')
        line2 = BoxLayout(size_hint =(0.8,None), height = '30sp')

        instr = Label(text=txt_instruction)
        lbl1 = Label(text = "Введіть ім'я:",halign = 'right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text = "Введіть вік:")
        self.in_age = TextInput(text = '7', multiline = False)
        self.btn = Button(
            text = "Почати", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)

        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)
    def next(self):
        self.manager.current = 'pulse1'




class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstScr(name = 'instr'))
        sm.add_widget(PulseScr(name = 'pulse1'))
        sm.add_widget(CheckSits(name = 'sits'))
        sm.add_widget(PulseScr2(name = 'pulse2'))
        sm.add_widget(Result(name = 'result'))
        return sm
    
app = HeartCheck()
app.run()