from wtforms import Form, SubmitField,IntegerField,FloatField,StringField,TextAreaField,validators,DateTimeField
from flask_wtf.file import FileField,FileRequired,FileAllowed

class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    model = StringField('Model', [validators.DataRequired()])
    CPU_type = StringField('CPU_type', [validators.DataRequired()])
    chipset = StringField('Chipset', [validators.DataRequired()])
    mem_slots = StringField('Memory Slots', [validators.DataRequired()])
    max_mem = TextAreaField('Max Memory', [validators.DataRequired()])
    channels = TextAreaField('Channels', [validators.DataRequired()])
    PCI = TextAreaField('PCI', [validators.DataRequired()])
    storage = StringField('Storage', [validators.DataRequired()])
    audio_chipset = StringField('Audio Chipset', [validators.DataRequired()])
    audio_channels = TextAreaField('Audio Channels', [validators.DataRequired()])
    LAN_chipset = TextAreaField('LAN Chipset', [validators.DataRequired()])
    form_factor = StringField('Form Factor', [validators.DataRequired()])
    features = TextAreaField('Features', [validators.DataRequired()])
    release_date = DateTimeField('Release Date', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])

class AddRam(Form):
    name = StringField('Name', [validators.DataRequired()])
    model = StringField('Model', [validators.DataRequired()])
    series = StringField('Series', [validators.DataRequired()])
    capacity = StringField('Capacity', [validators.DataRequired()])
    mem_type = StringField('Memory Type', [validators.DataRequired()])
    speed = StringField('Speed', [validators.DataRequired()])
    voltage = StringField('Voltage', [validators.DataRequired()])
    buff_reg = StringField('Buffered/Registered' , [validators.DataRequired()])
    heatspreader = StringField('Heat Spreader', [validators.DataRequired()])
    features = TextAreaField('Features', [validators.DataRequired()])
    date_released = StringField('Release Date', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])


class AddCpu(Form):
    name = StringField('Name', [validators.DataRequired()])
    model = StringField('Model', [validators.DataRequired()])
    series = StringField('Series', [validators.DataRequired()])
    cpu_type = StringField('CPU Type', [validators.DataRequired()])
    socket_type = StringField('Socket Type', [validators.DataRequired()])
    num_core = StringField('# of Cores', [validators.DataRequired()])
    num_threads = StringField('# of Threads', [validators.DataRequired()])
    frequency = StringField('Frequency', [validators.DataRequired()])
    l1 = StringField('L1 Cache')
    l2 = StringField('L2 Cache')
    l3 = StringField('L3 Cache')
    Manufacturing_Tech = StringField('Manufacturing_Tech', [validators.DataRequired()])
    mem_type = StringField('Memory Type', [validators.DataRequired()])
    mem_channel = IntegerField('Memory Channel', [validators.DataRequired()])
    PCI_Revision = StringField('PCI Express Revision', [validators.DataRequired()])
    power = StringField('Thermal Design Power', [validators.DataRequired()])
    date_released = DateTimeField('Release Date', [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])

class addGraphicCARD(Form):
    name = StringField('Name', [validators.DataRequired()])
    model = StringField('Model', [validators.DataRequired()])
    interface = StringField('Interface', [validators.DataRequired()])
    Chipset_Manufacturer = StringField('Chipset Manufacturer', [validators.DataRequired()])
    GPU = StringField('GPU', [validators.DataRequired()])
    Boost_Clock = StringField('Boost_Clock', [validators.DataRequired()])
    Memory_Size = StringField('Memory_Size', [validators.DataRequired()])
    Memory_Interface = StringField('Memory_Interface', [validators.DataRequired()])
    Memory_Type = StringField('Memory Type', [validators.DataRequired()])
    DirectX = StringField('DirectX', [validators.DataRequired()])
    HDMI = StringField('HDMI', [validators.DataRequired()])
    Multi_Monitor = StringField('Multi_Monitor', [validators.DataRequired()])
    Display_Port = StringField('Display_Port', [validators.DataRequired()])
    max_res = StringField('MAX. Resolution', [validators.DataRequired()])
    vr_ready = StringField('VR Ready', [validators.DataRequired()])
    cooler =  StringField('Cooler', [validators.DataRequired()])
    power = StringField('Power', [validators.DataRequired()])
    req = StringField('Requirements', [validators.DataRequired()])
    power_connector = StringField('Power Connector', [validators.DataRequired()])
    features = TextAreaField('Features', [validators.DataRequired()])
    dimentions = StringField('Dimentions', [validators.DataRequired()])
    date_released = date_released = DateTimeField('Release Date', [validators.DataRequired()])
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])

class addCASE(Form):
    name = StringField('Name', [validators.DataRequired()])
    model = StringField('Model', [validators.DataRequired()])
    series = StringField('Series', [validators.DataRequired()])
    case_type = StringField('Case Type', [validators.DataRequired()])
    color = StringField('Color', [validators.DataRequired()])
    case_material = StringField('Case Material', [validators.DataRequired()])
    power_supply = StringField('Power Supply', [validators.DataRequired()])
    Motherboard_Compatibility = StringField('Motherboard_Compatibility', [validators.DataRequired()])
    External_525_Drive_Bays = StringField('External 5.25" Drive Bays', [validators.DataRequired()])
    External_35_Drive_Bays = StringField('External 3.5" Drive Bays', [validators.DataRequired()])
    External_25_Drive_Bays = StringField('External 2.5" Drive Bays', [validators.DataRequired()])
    Expansion_Slots = StringField('Expansion Slots', [validators.DataRequired()])
    Front_Ports = StringField('Front Ports', [validators.DataRequired()])
    Fan_Options = StringField('Fan Options', [validators.DataRequired()])
    Radiator_Options = StringField('Radiator Options', [validators.DataRequired()])
    Max_GPU_Length= StringField('Max_GPU_Length', [validators.DataRequired()])
    Max_CPU_Cooler_Height  =  StringField('Max_CPU_Cooler_Height', [validators.DataRequired()])
    features  =  StringField('Features', [validators.DataRequired()])
    Dimensions_HxWxD = StringField('Dimensions (HxWxD)', [validators.DataRequired()])
    Weight = StringField('Weight', [validators.DataRequired()])
    date_released = date_released = DateTimeField('Release Date', [validators.DataRequired()])
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_2 = FileField('Image 2', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])
    image_3 = FileField('Image 3', validators=[ FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])

class addBUILD(Form):
    
    name = StringField('Name', [validators.DataRequired()])
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'Images only please'])

class Tempbuild(Form):
    name = StringField('Name', [validators.DataRequired()])