from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (14 / 255, 61 / 255, 76 / 255, 0)


class ang(BoxLayout):
    def calc(self):
        
        geiv_1 = self.ids.geiv_1.text
        geiv_2 = self.ids.geiv_2.text
        geiv_3 = self.ids.geiv_3.text
        geiv_4 = self.ids.geiv_4.text
        i_cx1 = self.ids.i_cx1.text
        i_cx2 = self.ids.i_cx2.text
        i_cx3 = self.ids.i_cx3.text
        i_cx4 = self.ids.i_cx4.text

        if not geiv_1 or not i_cx1:
            dif_cx1 = ''
            ajuste_cx1 = ''
        else:
            geiv_1 = float(self.ids.geiv_1.text)
            i_cx1 = float(self.ids.i_cx1.text)
            dif_cx1 = round(2.50 - geiv_1,2)
            ajuste_cx1 = round(i_cx1 + dif_cx1,2)
        
        if not geiv_2 or not i_cx2:
            dif_cx2 = ''
            ajuste_cx2 = ''
        else:
            geiv_2 = float(self.ids.geiv_2.text)
            i_cx2 = float(self.ids.i_cx2.text)
            dif_cx2 = round(2.83 - geiv_2,2)
            ajuste_cx2 = round(i_cx2 + dif_cx2,2)
        
        if not geiv_3 or not i_cx3:
            dif_cx3 = ''
            ajuste_cx3 = ''
        else:
            geiv_3 = float(self.ids.geiv_3.text)
            i_cx3 = float(self.ids.i_cx3.text)
            dif_cx3 = round(3.17 - geiv_3,2)
            ajuste_cx3 = round(i_cx3 + dif_cx3,2)
        
        if not geiv_4 or not i_cx4:
            dif_cx4 = ''
            ajuste_cx4 = ''
        else:
            geiv_4 = float(self.ids.geiv_4.text)
            i_cx4 = float(self.ids.i_cx4.text)
            dif_cx4 = round(3.50 - geiv_4,2)
            ajuste_cx4 = round(i_cx4 + dif_cx4,2)       
        
        self.ids.dif_cx1.text = str(dif_cx1)
        self.ids.dif_cx2.text = str(dif_cx2)
        self.ids.dif_cx3.text = str(dif_cx3)
        self.ids.dif_cx4.text = str(dif_cx4)
        
        self.ids.ajuste_cx1.text = str(ajuste_cx1)
        self.ids.ajuste_cx2.text = str(ajuste_cx2)
        self.ids.ajuste_cx3.text = str(ajuste_cx3)
        self.ids.ajuste_cx4.text = str(ajuste_cx4)



class angulo(App):
    def build(self):
        return ang()


angulo().run()

#Soli Deo Gloria
