import inspect
##from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display
import Designer
show = Designer.show

class DesignInteract(object):   # haven't yet thought of a good name
    
    def __init__(self,callable=None):
        self.section = None
        self.data = {}
        self.widgets = {}
        self.properties = set()
        self.widget_list = []
        self.output_widget = None
        self.main_widget = None
        self.dsg_widget = None
        self.compute_button = None
        self.defaults = {}
        if callable:
            self._install_callable(callable)
        
    def setDefaults(self,**kwargs):
        self.defaults.update(kwargs)
    
    def _build(self):
        self.output_widget = widgets.Output(layout={'border': '1px solid black'})
        with self.output_widget:
            b = widgets.Button(description='Compute!',tooltip='Click to perform calculations')
            b.on_click(self._on_compute_clicked)
            self.compute_button = b
            allwidg = widgets.VBox(self.widget_list+[b])
            self.main_widget = allwidg
    
    def _on_compute_clicked(self,b):
        """Examine the arguments of the callable and drag them out of data."""
        self.output_widget.clear_output()
        with self.output_widget:
            for key,w in self.widgets.items():
                self.data[key] = w.value
            self.callable(*[self.data[k] for k in self.callable_args])
            
    def _install_callable(self,callable):
        args = inspect.getfullargspec(callable)
        assert args.varargs is None and args.varkw is None
        if args.defaults:
            for k,v in zip(args.args[len(args.args)-len(args.defaults):],args.defaults):
                self.defaults[k] = v
        self.callable_args = args.args
        self.callable = callable
        
    def interact(self,callable=None):
        self._build()
        if callable:
            self._install_callable(callable)
        self._updateWidgetValues()
        display(self.main_widget)
        display(self.output_widget)
        
    def _updateWidgetValues(self,keys=[]):
        if not keys:
            keys = self.widgets.keys()
        for k in keys:
            w = self.widgets[k]
            if k in self.data:
                w.value = self.data[k]
            elif k in self.defaults:
                w.value = self.defaults[k]
        
    def _floatWidgets(self,text):
        ans = []
        for key in text.split(','):
            key = key.strip()
            val = 0.
            if '=' in key:
                k,v = key.split('=',1)
                key = k.strip()
                val = float(eval(v))
                self.defaults[key] = val
            w = widgets.FloatText(value=val,description=key+':')
            ans.append((key,w))
        return ans
    
    def _on_load_clicked(self,b):
        with self.output_widget:
            Dsg = self.dsg_widget.value
            section = Designer.SST.section(Dsg)
            for p in self.properties:
                self.data[p] = section[p]
            self.data['Dsg'] = Dsg
            self._updateWidgetValues(self.properties)
            
    def defWidgets(self,text,properties=False):
        wlist = []
        if properties:
            dwidg = widgets.Text(value=properties,
                               placeholder='Shape Designation',
                               description='Dsg:',
                              tooltip='A shape designation to lookup for values.')
            pbut = widgets.Button(description='Load Properties',
                                   tooltip='Click to load properties into entries below.')
            pbut.on_click(self._on_load_clicked)
            top = widgets.HBox([dwidg,pbut])
            wlist.append(top)
            self.dsg_widget = dwidg
        for key,w in self._floatWidgets(text):
            self.widgets[key] = w
            if properties:
                self.properties.add(key)
            wlist.append(w)
        self.widget_list.extend(wlist)
        
    def show(self,text):
        Designer.show(text,data=self.data)
