#sim.py
start = 0 * 60 *60
end = 24 * 60 * 60

#TODO check if the bus departure is shortened based on simulation time
#Giving it an extra two hours for the end time of the busses
upper_bound_delay = end - start + (2*60*60)
#after "end of simulation"

duration = 24* 60 #24 hours + 2 hours to account for the buses end time
pct_stops_as_sensors = 30
no_of_seeds = 100
msg_gen_rate_range = (1, 2*60) #in minutes
network_file_list = [
    'louisville.zip'
    #'cht.zip'
]
network_file = None #not sure what this line is for. I wonder


#sample_gateways = 
cht_gateways = {
        "greedy_sc" : [
            '778638', '778671', '778650', '778737'
        ],
        "betweenness" : [
            '778627', '778601', '778637', '778638', '778819', '778600', '778641', '778771', '778656', '778658',
            '778655', '778657',
            '778604', '778807', '778671', '778814', '778828', '778750', '778482', '778825', '778826', '778630',
            '778634', '778653','778732'
            ],
        "in_degree" : [
            '778648', '778604', '778627', '778634', '778653', '778449', '778454', '778554', '778563', '778570',
            '778601', '778636', '778638', '778641', '778651', '778671', '778697', '778737'
        ],
        "celf" : [
            '778638', '778671', '778806', '778650', '778860', '778798', '778563', '778757', '778784',
             '778926', '778959', '778467', '778818', '778620', '778655'
    ],
        "celf_old" : [
                           '778638', '779010', '778672', '778657', '778884', '778563', '778627',
                           '778928', '778465', '778923', '778711', '778759', '778950', '779004', '778496'
                          ],
        "mcmd" : {
             '0.0': ['778638', '778671', '778806', '778650', '778860'],
             '0.2': ['778638', '778671', '778806', '778650', '778860'],
             '0.4': ['778638', '778671', '778806', '778650', '778860'],
             '0.6': ['778638', '778671', '778650', '778737', '778784'],
             '0.8': ['778638', '778671', '778650', '778737', '778784'],
             '1.0': ['778638', '778671', '778650', '778737', '778784']
        }
    }

louisville_gateways = {
         "greedy_sc" : ['2865', '3795', '99911', '221', '44140', '14788', '1325', '50410', '18270', '20425', '9780', '42245', '39411'] ,
         "celf" : [
             '3795', '22948', '2865', '10240', '13405', '9210', '31725', '3260', '39424', '15110', '19720', '1480', '21276', '15635', '22940'],
         "betweenness" : ['2865', '1295', '17480', '17485', '216', '17500', '3795', '3810', '221', '211', '226', '14970', '16000', '1410', '1415', '3790', '2860', '14965', '5615', '14950', '3820', '1420', '1325', '17860', '17865', '17870', '17880', '1315', '16005', '1305', '1310', '3260', '14960', '3265', '3275', '19425', '3830', '19485', '3845', '15800', '15810', '15815', '16162', '13540', '13550', '1450', '1460', '1465', '1475', '1485', '17885', '17890', '13555', '13565', '2795', '2825', '2835', '2845', '2850', '2855', '4320', '4325', '4330', '9250', '9255', '9263', '38443', '38445', '3931', '3285', '3295', '19410', '19415', '4332', '70020', '70025', '14715', '16170', '16175', '16185', '17470', '17475', '25925', '22955', '40875', '30150', '15435', '15440', '14955', '25570', '25575', '1405', '24925', '14690', '14695', '14700', '4075', '4080', '4085', '4090', '3938', '18080', '18090', '46048', '6730', '6740', '6745', '6750', '3205', '3210', '10060', '22948', '25615', '25620', '24930', '70040', '24940', '24945', '24950', '24955', '24960', '24970', '24975', '24935', '3310', '15785', '4715', '24985', '24990', '25000', '25005', '25015', '35975', '35610', '35980', '4685', '4690', '4710', '3935', '17493', '1326', '46040', '37470', '36703', '9650', '9655', '9660', '9665', '9670', '9675', '9680', '15635', '1280', '21885', '29460', '29470', '29475', '29480', '29485', '29490', '2750', '2755', '2765', '2770', '2775', '2785', '8280', '8290', '8210', '1395', '39901', '39903', '24905', '3315', '3320', '3325', '24910', '24915', '9245', '8295', '25510', '99901', '29500', '29505', '29510', '29520', '29525', '8606', '43338', '2790', '5610', '6385', '6395', '6396', '6410', '14788', '13489', '14790', '14795', '44140', '10560', '10565', '10570', '261', '18165', '18170', '18180', '18185', '18190', '18195', '24895', '24900', '8215', '8220', '8225', '8230', '18780', '19225', '1425', '6390', '6435', '14985', '14990', '15005', '15010', '15025', '15035', '15045', '15050', '15055', '1490', '1495', '1510', '1520', '1530', '1535', '1540', '1550', '1555', '1570', '1571', '1811', '60000', '9210', '99910', '33015', '50410', '3518', '10050', '10055', '39411', '39424', '39509', '33020', '33030', '8235', '8240', '8245', '8250', '8255', '8265', '8270', '18660', '18665', '18670', '18675', '25230', '25235', '25240', '25245', '25250', '32210', '32215', '32220', '32225', '32230', '32240', '32245', '99968', '32350', '32355', '32370', '32375', '32380', '32385', '32390', '32400', '25380', '25385', '25390', '25395', '25400', '25405', '9685', '9690', '9700', '9705', '9720', '9725', '19417', '19420', '14725', '16160', '2692', '3036', '2730', '2745', '13770', '13785', '13795', '16125', '16130', '16135', '16145', '16150', '16760', '16775', '16780', '16785', '13760', '15925', '15930', '15935', '15940', '15945', '29205', '29210', '29215', '29220', '29225', '29235', '18270', '18275', '18280', '18300', '18305', '18315', '18325', '15950', '15960', '15965', '15970', '15975', '15980', '15985', '29165', '15990', '15995', '50405', '99946', '6415', '6420', '13800', '13805', '13810', '13815', '13820', '13825', '13830', '13835', '30698', '19430', '18790', '18800', '19435', '19440', '19455', '11570', '26565', '14480', '14490', '14495', '14500', '14505', '14510', '14515', '14520', '9290', '33035', '39505', '39508', '15305', '15310', '15315', '15320', '15325', '15330', '15335', '15340', '15345', '15350', '15355', '15365', '15370', '15375', '15380', '15385', '25145', '25150', '25155', '25160', '25165', '25170', '25180', '25190', '25195', '25200', '25210', '25212', '25215', '25220', '15070', '15075', '15085', '15090', '15095', '15105', '15110', '15115', '15120', '15125', '15130', '15135', '15140', '25410', '25415', '25430', '25435', '25445', '25450', '25455', '25460', '25470', '25480', '25485', '25490', '25495', '25500', '8015', '8020', '9992', '12910', '3404', '50035', '18680', '18685', '18695', '18700', '18710', '18711', '27270', '26562', '3780', '3785', '3970', '12185', '12190', '44130', '50325'],
         "in_degree" : ['211', '15635', '16000', '24905', '2860', '60075', '8606', '99911', '10305', '1280', '12910', '1315', '14950', '14960', '15440', '15565', '16715', '17860', '18080', '18660', '19425', '19640', '22948', '22955', '25615', '25925', '29171', '3240', '3790', '3795', '3938', '39411', '42465', '44140', '5610', '5615', '7425', '9210', '9290', '10005', '10038', '10040', '10060', '10240', '10335', '10360', '10557', '10560', '10605', '10735', '10814', '1097', '11025', '1155', '11570', '11580', '11590', '11600', '11745', '1195', '11960', '12185', '1220', '12740', '12760', '1325', '1330', '1338', '13405', '13665', '13760', '13770', '13785', '13800', '1395', '1405', '14070', '1410', '1425', '14255', '14480', '1450', '14525', '14545', '14570', '14590', '1460', '14640', '14690', '14715', '1475', '14788', '14801', '1485', '14965', '14970', '14985', '15070', '15085', '15305', '15390', '15435', '15785', '15800', '15890', '15925', '16049', '16070', '16090', '16125', '16160', '16170', '16185', '16295', '16365', '16775', '16880', '17090', '17300', '17470', '17480', '17580', '17590', '17610', '17620', '17635', '17725', '17745', '17840', '17880', '1805', '18110', '18270', '18300', '18760', '18780', '19060', '19225', '19410', '19490', '19505', '19515', '19525', '19615', '19625', '19635', '19720', '20425', '20450', '20586', '20725', '20980', '21110', '21125', '21276', '21292', '216', '21610', '21635', '21675', '21685', '21745', '21750', '21790', '21840', '21850', '21885', '221', '22258', '22315', '22645', '22935', '22940', '22980', '22995', '23005', '23030', '23035', '23070', '23080', '23110', '2315', '23175', '23190', '23205', '23280', '23290', '23310', '23420', '23700', '23820', '23985', '23990', '241', '24670', '24680', '24690', '24700', '24735', '24755', '24800', '24850', '24860', '24875', '24895', '24925', '24940', '24970', '25030', '25145', '25230', '2535', '25380', '25525', '25555', '25870', '26055', '261', '26280', '26400', '26550', '26553', '26565', '2692', '2730', '2750', '2795', '2825', '2835', '2845', '286', '2865', '29205', '29360', '29370', '29460', '303'] 
     }

