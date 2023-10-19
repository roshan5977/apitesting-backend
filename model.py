from sqlalchemy import Boolean, Column, String, Integer, DateTime, Time, ForeignKey
from database import Base
from sqlalchemy.orm import relationship










# class Application(Base):
#     __tablename__ = "application"
#     application_id=Column(Integer, primary_key=True, autoincrement=True)
#     base_url=Column(String)


# class Path(Base): 
#     path_id=Column(Integer, primary_key=True, autoincrement=True)
#     path_name = Column(String)
#     method_type = Column(String)
#     tags = Column(String)
#     summary = Column(String)


# class RequestBody(Base):
#     req_body_id = Column(Integer, primary_key=True, autoincrement=True)
    




# class PathVariable(Base):
#     path_var_id=Column(Integer, primary_key=True, autoincrement=True)
#     path_var=Column(String)
#     path_var_type=Column(String)
#     ispath_var_mandatory=Column(String)



# class RequestParam(Base):
#     req_param_id=Column(Integer, primary_key=True, autoincrement=True)
#     req_param=Column(String)
#     req_param_type=Column(String)
#     isreq_param_mandatory=Column(String)


# class AuthorisationToken(Base):
#     auth_id: Column(Integer, primary_key=True, autoincrement=True)
#     auth_token: Column(String)



# class Schema(Base):
#     schema_id: Column(Integer, primary_key=True, autoincrement=True)
#     schema_title: Column(String)


# class SchemaProperties(Base):
#     schema_property_id: Column(Integer, primary_key=True, autoincrement=True)
#     schema_property_name: Column(String)
#     schema_property_type: Column(String)
#     is_property_required: Column(Boolean)

