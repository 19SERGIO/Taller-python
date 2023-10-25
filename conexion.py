import pymongo

conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd= conexion["apropiacion-sensores"]
usuarios=bd["usuarios"]
sensores=bd["sensores"]
