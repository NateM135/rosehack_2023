# <option value="Developer">Developer</option>

d = {
    "Agriculture": "https://cdn.discordapp.com/attachments/989196355199205456/1064182033498263552/agriculture.png",
    "Construction": "https://cdn.discordapp.com/attachments/989196355199205456/1064182033766682674/construction.png",
    "Culture Sports and Entertainment": "https://media.discordapp.net/attachments/989196355199205456/1064182034026725426/Culture_Sports_and_Entertainment.png",
    "Education": "https://cdn.discordapp.com/attachments/989196355199205456/1064182034492313691/Education.png",
    "Employed": "https://cdn.discordapp.com/attachments/989196355199205456/1064182034878173234/Employed_Persons_Total.png",
    "Financial Intermediation": "https://cdn.discordapp.com/attachments/989196355199205456/1064182035213734029/Financial_Intermediation.png",
    "Health and Social Service": "https://cdn.discordapp.com/attachments/989196355199205456/1064182035587010560/Health_and_Social_Service.png",
    "Hotels and Catering Services": "https://cdn.discordapp.com/attachments/989196355199205456/1064182036044185611/Hotels_and_Catering_Services.png",
    "Information Transmission, Software and Information Technology": "https://cdn.discordapp.com/attachments/989196355199205456/1064182036329418762/Information_Transmission._Software_and_Information_Technology.png",
    "Leasing and Business Services": "https://cdn.discordapp.com/attachments/989196355199205456/1064182073759375400/Leasing_and_Business_Services.png",
    "Management of Water Conservancy Environment and Public Facilities": "https://cdn.discordapp.com/attachments/989196355199205456/1064182073939742770/Management_of_Water_Conservancy_Environment_and_Public_Facilities.png",
    "Manufacturing":"https://cdn.discordapp.com/attachments/989196355199205456/1064182074141048863/Manufacturing.png",
    "Mining":"https://cdn.discordapp.com/attachments/989196355199205456/1064182074317217822/Mining.png",
    "Production and Supply of Electricity Heat Gas and Water":"https://cdn.discordapp.com/attachments/989196355199205456/1064182074522751006/Production_and_Supply_of_Electricity_Heat_Gas_and_Water.png",
}

for k in d:
    print(f'<option value="{k}">{k}</option>')