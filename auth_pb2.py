# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\"B\n\rSignUpRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"C\n\x0eSignUpResponse\x12\x0f\n\x07\x62oolean\x18\x01 \x01(\x08\x12\x10\n\x08response\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"B\n\rLoginResponse\x12\x0f\n\x07\x62oolean\x18\x01 \x01(\x08\x12\x10\n\x08response\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x32:\n\rSignUpService\x12)\n\x06signUp\x12\x0e.SignUpRequest\x1a\x0f.SignUpResponse26\n\x0cLoginService\x12&\n\x05login\x12\r.LoginRequest\x1a\x0e.LoginResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIGNUPREQUEST._serialized_start=14
  _SIGNUPREQUEST._serialized_end=80
  _SIGNUPRESPONSE._serialized_start=82
  _SIGNUPRESPONSE._serialized_end=149
  _LOGINREQUEST._serialized_start=151
  _LOGINREQUEST._serialized_end=198
  _LOGINRESPONSE._serialized_start=200
  _LOGINRESPONSE._serialized_end=266
  _SIGNUPSERVICE._serialized_start=268
  _SIGNUPSERVICE._serialized_end=326
  _LOGINSERVICE._serialized_start=328
  _LOGINSERVICE._serialized_end=382
# @@protoc_insertion_point(module_scope)