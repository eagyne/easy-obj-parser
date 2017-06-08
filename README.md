# easy-obj-parser
an easy program. parser obj file to json  
临时写的一个将OBJ模型文件转换成JSON格式的Python转换器

You can export easy models from Blender as obj file.  
从Blender中将简单的模型导出为OBJ格式

After exporting your model to the OBJ format, try to parse the obj file to JSON format using:  
拿到OBJ格式后,通过这个脚本弄成JSON描述的模型:

``` python
  python parse_obj2json model.obj
```
Then you'll have a model.json file which contains vertices, indices, normals and normals_idx.  
得到的JSON中包含的数据只有顶点、顶点索引、法线、法线索引

Just load the model into your WebGL scene through model.json  
然后可以把模型用到你的WebGL程序中了。

