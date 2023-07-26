import names
import randomname
import random
import json
import datetime

from happytransformer import HappyTextToText
from happytransformer import TTSettings

#timmy the robo - generator

countries = [
    ('US', 'United States'),('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'),
    ('AG', 'Antigua And Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),('BY', 'Belarus'),('BE', 'Belgium'),('BZ', 'Belize'),('BJ', 'Benin'),('BM', 'Bermuda'),('BT', 'Bhutan'),('BO', 'Bolivia'),('BA', 'Bosnia And Herzegowina'),
    ('BW', 'Botswana'),('BV', 'Bouvet Island'),('BR', 'Brazil'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'),
    ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),('CF', 'Central African Rep'),('TD', 'Chad'),('CL', 'Chile'),('CN', 'China'),('CX', 'Christmas Island'),('CC', 'Cocos Islands'),('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),('CR', 'Costa Rica'),('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),('TP', 'East Timor'),('EC', 'Ecuador'),('EG', 'Egypt'),('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'),
    ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'), ('FI', 'Finland'),('FR', 'France'),('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('GA', 'Gabon'), ('GM', 'Gambia'),
    ('GE', 'Georgia'),('DE', 'Germany'),('GH', 'Ghana'),('GI', 'Gibraltar'),('GR', 'Greece'),('GL', 'Greenland'),('GD', 'Grenada'),
    ('GU', 'Guam'),('GT', 'Guatemala'),('GN', 'Guinea'),('GW', 'Guinea-bissau'),('GY', 'Guyana'),('HT', 'Haiti'),('HN', 'Honduras'),('HK', 'Hong Kong'),('HU', 'Hungary'),
    ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'),('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', 'Korea (North)'), ('KR', 'Korea (South)'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'),
    ('LR', 'Liberia'),('LY', 'Libya'),('LI', 'Liechtenstein'),('LT', 'Lithuania'),('LU', 'Luxembourg'),('MO', 'Macau'),('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'),
    ('ML', 'Mali'), ('MT', 'Malta'),('MH', 'Marshall Islands'),('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia'),('MD', 'Moldova'),
    ('MC', 'Monaco'),('MN', 'Mongolia'),('MS', 'Montserrat'),  ('MA', 'Morocco'),  ('MZ', 'Mozambique'),  ('MM', 'Myanmar'),  ('NA', 'Namibia'),  ('NR', 'Nauru'),  ('NP', 'Nepal'), ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),  ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),  ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'),  ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('KN', 'Saint Kitts And Nevis'), ('LC', 'Saint Lucia'), ('VC', 'St Vincent/Grenadines'),
    ('WS', 'Samoa'),  ('SM', 'San Marino'),  ('ST', 'Sao Tome'),  ('SA', 'Saudi Arabia'),  ('SN', 'Senegal'),  ('SC', 'Seychelles'),  ('SL', 'Sierra Leone'),  ('SG', 'Singapore'),  ('SK', 'Slovakia'),  ('SI', 'Slovenia'), ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),  ('ZA', 'South Africa'),  ('ES', 'Spain'),  ('LK', 'Sri Lanka'),  ('SD', 'Sudan'),  
    ('SZ', 'Swaziland'),('SE', 'Sweden'),('CH', 'Switzerland'),('SY', 'Syrian Arab Republic'),('TW', 'Taiwan'),('TJ', 'Tajikistan'),('TZ', 'Tanzania'),
    ('TH', 'Thailand'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'),
    ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('UK', 'United Kingdom'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatican City State'), ('VE', 'Venezuela'),
    ('VN', 'Viet Nam'), ('VG', 'Virgin Islands (British)'), ('VI', 'Virgin Islands (U.S.)'), ('YE', 'Yemen'), ('YU', 'Yugoslavia'), ('ZR', 'Zaire'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')
]


def listToString(s):
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1

# create function accepting a single parameter, the year as a four digit number
def get_random_birthday(age):
   today = datetime.date.today()
   current_year = today.year
   birthyear= current_year - age
   
   # try to get a date
   try:
       states= datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), birthyear), '%j %Y')
       states= str(states)
       states= states.replace("00:00:00","")
       return states

   # if the value happens to be in the leap year range, try again
   except ValueError:
      get_random_date(year)


def identity():
   fullname = names.get_full_name()
   fullname1 = f'NAME: {fullname}\n'
   age = random.randint(1, 100)
   if age <= 3:
      global label
      label = "Toddler"
   elif age > 3 and age <= 5:
      label = "Preschool Student"
   elif age > 6 and age <= 13:
      label = "Elementary Student"
   elif age > 14 and age <= 17:
      label = "Highschool Student"
   elif age > 18 and age <= 25:
      label = "Young Adult"
   elif age > 26 and age <= 35:
      label = "Young Adult - Early Career"
   elif age > 36 and age <= 45:
      label = "Adult - Mid Career"
   elif age > 46 and age <= 59:
      label = "Adult - Late Career"
   elif age >= 60:
      label = "Senior"
   else: pass
   
   back = f"STATUS: {label}\n"
   
   age1 =f'AGE: {age}\n'
   country_orgin= random.choice(countries)
   country= country_orgin[1]
   country_orgin1=f"COUNTRY: {country}\n"

   favorite=randomname.get_name(noun=('food'))
   favorite_food= f"FAVORITE FOOD: {favorite}\n"
   

   least= randomname.get_name(noun=('food'))
   least_favortite_food= f"LEAST FAVORITE FOOD: {least}\n\n\n"

   birthday= get_random_birthday(age)
   birthday1= f"BIRTHDAY: {birthday}\n"

   r=[]
   for num in range(15):
      code = randomname.generate( ('n/corporate', 'n/food', 'n/corporate_job',
                                   'n/sports', 'n/fish', 'n/design' , 'n/dogs', 'n/cats','n/birds',
                                   "n/condiments","n/meat","n/seasonings"))
      r.append(code)


   info = fullname1 + age1 + back + country_orgin1 + birthday1 + favorite_food +  least_favortite_food

#needs improvement for random backstory generator
   template= f"{fullname} is an {age} year old {label}. From {country_orgin[1]} and born on {birthday[1]}. The {r[0]} have something with the associates with {r[1]}."
#To correct the grammar
   happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
   text = "gec: " + template
   settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
   result = happy_tt.generate_text(text, args=settings)
   return info +  result.text




class roboTim:
    '''Character Robo Timmy'''
    species="Mousewanderer's robot"


    def __int__(self,told):
        self.told=told
  
# used to get quotes 
    def Isubmit(self):
        return identity()

    def gramCor(self,told):
        template = told
        happy_tt = HappyTextToText("T5", "prithivida/grammar_error_correcter_v1")
        text = "gec: " + template
        settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
        result = happy_tt.generate_text(text, args=settings)
        return result.text
        
        
        
        



