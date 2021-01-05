from django.conf.urls import url
from django.contrib import admin
from .views import constructor, warehouse, material


urlpatterns = [
    url(r'^constructor$', constructor.constructor, name='constructor'), 
    # url(r'^constructor/add$', constructor.add, name='constructor_add'), 
    url(r'^constructor/del$', constructor.delete, name='constructor_del'), 
    # url(r'^constructor/edit$', constructor.edit, name='constructor_edit'), 
    url(r'^constructor/allow$', constructor.allow, name='constructor_allow'), 
    url(r'^constructor/forbid$', constructor.forbid, name='constructor_forbid'), 
    url(r'^constructor/search_data$', constructor.search_data, name='constructor_search_data'), 
    url(r'^constructor/load_data$', constructor.load_data, name='constructor_load_data'), 
    url(r'^constructor/down_excel_template$', constructor.down_excel_template, name='constructor_down_excel_template'), 
    url(r'^constructor/upload_excel$', constructor.upload_excel, name='constructor_upload_excel'), 
    url(r'^constructor/import_data$', constructor.import_data, name='constructor_import_data'), 
    url(r'^constructor/export_excel$', constructor.export_excel, name='constructor_export_excel'), 
    url(r'^constructor/list$', constructor.lists, name='constructor_list'),
    url(r'^constructor/tree$', constructor.tree, name='constructor_tree'), 

    url(r'^warehouse$', warehouse.warehouse, name='warehouse'), 
    # url(r'^warehouse/add$', warehouse.add, name='warehouse_add'), 
    url(r'^warehouse/del$', warehouse.delete, name='warehouse_del'), 
    # url(r'^warehouse/edit$', warehouse.edit, name='warehouse_edit'), 
    url(r'^warehouse/allow$', warehouse.allow, name='warehouse_allow'), 
    url(r'^warehouse/forbid$', warehouse.forbid, name='warehouse_forbid'), 
    url(r'^warehouse/search_data$', warehouse.search_data, name='warehouse_search_data'), 
    url(r'^warehouse/load_data$', warehouse.load_data, name='warehouse_load_data'), 
    url(r'^warehouse/down_excel_template$', warehouse.down_excel_template, name='warehouse_down_excel_template'), 
    url(r'^warehouse/upload_excel$', warehouse.upload_excel, name='warehouse_upload_excel'), 
    url(r'^warehouse/import_data$', warehouse.import_data, name='warehouse_import_data'), 
    url(r'^warehouse/export_excel$', warehouse.export_excel, name='warehouse_export_excel'), 

    url(r'^material$', material.material, name='material'), 
    # url(r'^material/add$', material.add, name='material_add'), 
    url(r'^material/del$', material.delete, name='material_del'), 
    # url(r'^material/edit$', material.edit, name='material_edit'), 
    url(r'^material/allow$', material.allow, name='material_allow'), 
    url(r'^material/forbid$', material.forbid, name='material_forbid'), 
    url(r'^material/search_data$', material.search_data, name='material_search_data'), 
    url(r'^material/load_data$', material.load_data, name='material_load_data'), 
    url(r'^material/down_excel_template$', material.down_excel_template, name='material_down_excel_template'), 
    url(r'^material/upload_excel$', material.upload_excel, name='material_upload_excel'), 
    url(r'^material/import_data$', material.import_data, name='material_import_data'), 
    url(r'^material/export_excel$', material.export_excel, name='material_export_excel'), 

]
