from steve import Assets, Universe

 
# print Universe.system['IWZ3-C'].constellation.name
# print Universe.system['IWZ3-C'].region.uid
# print Universe.system['IWZ3-C'].uid
#  
# _type = Assets.type['Tritanium']
# print _type.name
# print _type.maxProductionLimit
#  
# _type = Assets.type['75mm Carbide Railgun I']
# print _type.name
# print _type.uid
# print _type.maxProductionLimit
# print _type.marketGroup
# print _type.metaType
# print '>>>', _type.hasBPO
# print _type.parentType.name
# # print _type.bpo.name
# for x, y in _type.bom:
#     print x.name, y 
#  
#  
# for key in Assets.type:
#     if isinstance(key, type('')) and 'array' in key.lower():
#         print key
#  
# _type = Assets.type[2534]
# print _type.name
# print _type.uid
# print _type.maxProductionLimit
# print '>>>', _type.hasBPO
#  
# print len(Assets.blueprint)
#  
# for x in Assets.getMarketGroupTypes('Small Armor Rigs'):
#     print x.name

#print Assets.blueprint[34214]