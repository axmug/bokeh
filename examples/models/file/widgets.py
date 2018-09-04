from __future__ import print_function

from datetime import date

from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.resources import INLINE
from bokeh.util.browser import view
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.layouts import Column, Row, Tabs, Panel
from bokeh.models.widgets import (
    Button, Toggle, Dropdown,
    CheckboxGroup, RadioGroup,
    CheckboxButtonGroup, RadioButtonGroup,
    TextInput, AutocompleteInput,
    Select, MultiSelect,
    Slider, RangeSlider, DateSlider, DateRangeSlider,
    DatePicker,
    Paragraph, Div, PreText,
    DataTable, TableColumn,
    StringFormatter, NumberFormatter,
    StringEditor, IntEditor, NumberEditor, SelectEditor,
)
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers
from bokeh.sampledata.autompg2 import autompg2 as mpg

button = Button(label="Button (disabled) - still has click event", button_type="primary", disabled=True)
toggle = Toggle(label="Toggle button", button_type="success")

menu = [("Item 1", "item_1_value"), ("Item 2", "item_2_value"), ("Item 3", "item_3_value")]

dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)
#dropdown_split = Dropdown(label="Split button", button_type="danger", menu=menu, default_value="default"))

checkbox_group = CheckboxGroup(labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])
radio_group = RadioGroup(labels=["Option 1", "Option 2", "Option 3"], active=0)

checkbox_button_group = CheckboxButtonGroup(labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])
radio_button_group = RadioButtonGroup(labels=["Option 1", "Option 2", "Option 3"], active=0)

text_input = TextInput(placeholder="Enter value ...")

completions = ["aaa", "aab", "aac", "baa", "caa"]
autocomplete_input = AutocompleteInput(placeholder="Enter value ...", completions=completions)

select = Select(options=["Option 1", "Option 2", "Option 3"])

multi_select = MultiSelect(options=["Option %d" % (i+1) for i in range(16)], size=6)

slider = Slider(value=10, start=0, end=100, step=0.5)

range_slider = RangeSlider(value=[10, 90], start=0, end=100, step=0.5)

#date_range_slider = DateRangeSlider(value=(date(2016, 1, 1), date(2016, 12, 31)))

date_picker = DatePicker(value=date(2017, 8, 1))

paragraph = Paragraph(text="some text")

div = Div(text="some <b>text</b>")

pre_text = PreText(text="some text")

def mk_tab(color):
    plot = figure(plot_width=300, plot_height=300)
    plot.scatter(flowers["petal_length"], flowers["petal_width"], color=color, fill_alpha=0.2, size=12)
    return Panel(title="Tab 1: %s" % color.capitalize(), child=plot)

tabs = Tabs(tabs=[mk_tab("red"), mk_tab("green"), mk_tab("blue")], width=400)

source = ColumnDataSource(data=mpg)
columns = [
    TableColumn(field="manufacturer",
                title="Manufacturer",
                editor=SelectEditor(options=sorted(mpg["manufacturer"].unique())),
                formatter=StringFormatter(font_style="bold")),
    TableColumn(field="model",
                title="Model",
                editor=StringEditor(completions=sorted(mpg["model"].unique()))),
    TableColumn(field="displ",
                title="Displacement",
                editor=NumberEditor(step=0.1),
                formatter=NumberFormatter(format="0.0")),
    TableColumn(field="year",
                title="Year",
                editor=IntEditor()),
    TableColumn(field="cyl",
                title="Cylinders",
                editor=IntEditor()),
    TableColumn(field="trans",
                title="Transmission",
                editor=SelectEditor(options=sorted(mpg["trans"].unique()))),
    TableColumn(field="drv",
                title="Drive",
                editor=SelectEditor(options=sorted(mpg["drv"].unique()))),
    TableColumn(field="class",
                title="Class",
                editor=SelectEditor(options=sorted(mpg["class"].unique()))),
    TableColumn(field="cty",
                title="City MPG",
                editor=IntEditor()),
    TableColumn(field="hwy",
                title="Highway MPG",
                editor=IntEditor()),
]
table = DataTable(source=source, columns=columns, editable=True, width=800)

widgets = Column(children=[
    Row(children=[
        Column(children=[
            button, toggle, dropdown, #dropdown_split,
            checkbox_group, radio_group,
            checkbox_button_group, radio_button_group,
        ]),
        Column(children=[
            text_input, autocomplete_input,
            select, multi_select,
            slider, range_slider, #date_range_slider,
            date_picker,
            paragraph, div, pre_text,
        ]),
        tabs,
    ]),
    table,
])

doc = Document()
#doc.add_root(widgets)

menu = [("Item 1", "1"), ("Item 2", "2"), ("Item 3", "3")]

#click = dict(js_property_callbacks={"change:clicks": [CustomJS(code="console.log(this.label)")]})

layout = Column(children=[
    Button(label="Disabled Default Button 1", button_type="default", disabled=True),
    Button(label="Primary Button 2", button_type="primary"),
    Button(label="Success Button 3", button_type="success"),

    Toggle(label="Warning Toggle 1", button_type="warning"),
    Toggle(label="Dange Toggle 2", button_type="danger"),
    Toggle(label="Default Toggle 3", button_type="default"),

    Dropdown(label="Success Dropdown 1", menu=menu, button_type="success"),
    Dropdown(label="Warning Dropdown 2", menu=menu, button_type="warning"),
    Dropdown(label="Danger Dropdown 3", menu=menu, button_type="danger"),

    CheckboxGroup(labels=["Checkbox Option 1", "Checkbox Option 2", "Checkbox Option 3"], active=[0, 1]),
    CheckboxGroup(labels=["Checkbox Option 4", "Checkbox Option 5", "Checkbox Option 6"], active=[1, 2]),
    CheckboxGroup(labels=["Checkbox Option 7", "Checkbox Option 8", "Checkbox Option 9"], active=[0, 2]),

    CheckboxGroup(labels=["Checkbox Option 1", "Checkbox Option 2", "Checkbox Option 3"], active=[0, 1], inline=True),
    CheckboxGroup(labels=["Checkbox Option 4", "Checkbox Option 5", "Checkbox Option 6"], active=[1, 2], inline=True),
    CheckboxGroup(labels=["Checkbox Option 7", "Checkbox Option 8", "Checkbox Option 9"], active=[0, 2], inline=True),

    RadioGroup(labels=["Radio Option 1", "Radio Option 2", "Radio Option 3"], active=0),
    RadioGroup(labels=["Radio Option 4", "Radio Option 5", "Radio Option 6"], active=1),
    RadioGroup(labels=["Radio Option 7", "Radio Option 8", "Radio Option 9"], active=2),

    RadioGroup(labels=["Radio Option 1", "Radio Option 2", "Radio Option 3"], active=0, inline=True),
    RadioGroup(labels=["Radio Option 4", "Radio Option 5", "Radio Option 6"], active=1, inline=True),
    RadioGroup(labels=["Radio Option 7", "Radio Option 8", "Radio Option 9"], active=2, inline=True),

    CheckboxButtonGroup(labels=["Checkbox Option 1", "Checkbox Option 2", "Checkbox Option 3"], active=[0, 1]),
    CheckboxButtonGroup(labels=["Checkbox Option 4", "Checkbox Option 5", "Checkbox Option 6"], active=[1, 2]),
    CheckboxButtonGroup(labels=["Checkbox Option 7", "Checkbox Option 8", "Checkbox Option 9"], active=[0, 2]),

    RadioButtonGroup(labels=["Radio Option 1", "Radio Option 2", "Radio Option 3"], active=0),
    RadioButtonGroup(labels=["Radio Option 4", "Radio Option 5", "Radio Option 6"], active=1),
    RadioButtonGroup(labels=["Radio Option 7", "Radio Option 8", "Radio Option 9"], active=2),

    TextInput(placeholder="TextInput 1"),
    TextInput(placeholder="TextInput 2"),
    TextInput(placeholder="TextInput 3"),

    AutocompleteInput(placeholder="AutocompleteInput 1 ...", completions=["aaa", "aab", "aac", "baa", "caa"]),

    Select(options=["Select Option 1", "Select Option 2", "Select Option 3"]),
    MultiSelect(options=["MultiSelect Option %d" % (i+1) for i in range(16)], size=6),

    #Paragraph(text="Paragraph 1"),
    #Paragraph(text="Paragraph 2"),
    #Paragraph(text="Paragraph 3"),

    #Div(text="Div 1"),
    #Div(text="Div 2"),
    #Div(text="Div 3"),

    #PreText(text="PreText 1"),
    #PreText(text="PreText 2"),
    #PreText(text="PreText 3"),

    DatePicker(value=date(2018, 9, 1)),
    DatePicker(value=date(2018, 9, 2)),
    DatePicker(value=date(2018, 9, 3)),

    Slider(value=10, start=0, end=100, step=0.5),
    RangeSlider(value=[20, 30], start=0, end=100, step=0.5),
    DateSlider(value=date(2018, 9, 1), start=date(2018, 1, 1), end=date(2018, 12, 31)),
    DateRangeSlider(value=(date(2018, 9, 1), date(2018, 9, 30)), start=date(2018, 1, 1), end=date(2018, 12, 31)),

    DataTable(source=source, columns=columns, editable=True), #, width=800),
])

doc.add_root(layout)

if __name__ == "__main__":
    doc.validate()
    filename = "widgets.html"
    with open(filename, "w") as f:
        f.write(file_html(doc, INLINE, "Widgets"))
    print("Wrote %s" % filename)
    view(filename)
