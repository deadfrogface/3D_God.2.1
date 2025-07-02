from PySide6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt

class CharacterEditorPanel(QWidget):
    def __init__(self, system):
        super().__init__()
        self.system = system
        layout = QVBoxLayout(self)
        self.sliders = {}
        for name, (minv,maxv) in [("Größe",(100,200)),("Gewicht",(0,100)),("Muskeln",(0,100))]:
            lbl = QLabel(f"{name}:")
            sld = QSlider(Qt.Horizontal)
            sld.setRange(minv,maxv)
            sld.setValue((minv+maxv)//2)
            sld.valueChanged.connect(lambda v,n=name:self.on_change(n,v))
            layout.addWidget(lbl)
            layout.addWidget(sld)
            self.sliders[name]=sld

    def on_change(self,name,value):
        print(f"CharacterEditor: {name} = {value}")
        self.system.set_body_attribute(name.lower(), value)