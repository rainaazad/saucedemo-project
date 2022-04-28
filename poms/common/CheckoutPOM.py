from flitscore.models import *

checkout_btn = obj(label='CHECKOUT', objtype='button')
firstname_tb = obj(label='First Name', around='placeholder', objtype='textbox', data_column='firstname')
lastname_tb = obj(label='Last Name', around='placeholder', objtype='textbox', data_column='lastname')
zip_tb = obj(label='Zip/Postal Code', around='placeholder', objtype='textbox', data_column='zip_postalcode')
continue_btn = obj(label='CONTINUE', objtype='button')
finish_btn = obj(label='FINISH', objtype='button')
