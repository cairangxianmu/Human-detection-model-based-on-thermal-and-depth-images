import os
import xml.dom.minidom

#path = "../test_image/" 
path1 = "../test_image/"
for file_path in os.listdir(path1):
  path2 = path1+file_path +"/"
  for file_name in os.listdir(path2):
    print(file_name)
    path = path2 + file_name
    name2 = file_name
    new_txtname=file_name.split('.')[0]
    name1 = file_path

    doc = xml.dom.minidom.Document()
    annotation = doc.createElement('annotation')

    folder = doc.createElement('folder')
    folder_text = doc.createTextNode('photo')
    annotation.appendChild(folder)
    folder.appendChild(folder_text)

    filename = doc.createElement('filename')
    filename_text = doc.createTextNode(name2)
    annotation.appendChild(filename)
    filename.appendChild(filename_text)

    path = doc.createElement('path')
    path_text = doc.createTextNode('../test_image_tf/'+file_name)
    annotation.appendChild(path)
    path.appendChild(path_text)

    doc.appendChild(annotation)

    source = doc.createElement('source')
    database = doc.createElement('database')
    database_text = doc.createTextNode('Unknown')
    source.appendChild(database)
    database.appendChild(database_text)
    annotation.appendChild(source)


    size = doc.createElement('size')
    width = doc.createElement('width')
    width_text = doc.createTextNode('45')
    height = doc.createElement('height')
    height_text = doc.createTextNode('45')
    depth = doc.createElement('depth')
    depth_text = doc.createTextNode('1')
    size.appendChild(width)
    width.appendChild(width_text)
    size.appendChild(height)
    height.appendChild(height_text)
    size.appendChild(depth)
    depth.appendChild(depth_text)
    annotation.appendChild(size)

    segmented = doc.createElement('segmented')
    segmented_text = doc.createTextNode('0')
    segmented.appendChild(segmented_text)
    annotation.appendChild(segmented)

    object1 = doc.createElement('object')
    name = doc.createElement('name')
    name_text = doc.createTextNode(name1)
    pose = doc.createElement('pose')
    pose_text = doc.createTextNode('Unspecified')
    truncated = doc.createElement('truncated')
    truncated_text = doc.createTextNode('1')
    difficult = doc.createElement('difficult')
    difficult_text = doc.createTextNode('0')
    object1.appendChild(name)
    name.appendChild(name_text)
    object1.appendChild(pose)
    pose.appendChild(pose_text)
    object1.appendChild(truncated)
    truncated.appendChild(truncated_text)
    object1.appendChild(difficult)
    difficult.appendChild(difficult_text)

    bndbox = doc.createElement("bndbox")
    xmin = doc.createElement("xmin")
    xmin_text = doc.createTextNode("1")
    ymin = doc.createElement("ymin")
    ymin_text = doc.createTextNode("1")
    xmax = doc.createElement("xmax")
    xmax_text = doc.createTextNode("44")
    ymax = doc.createElement("ymax")
    ymax_text = doc.createTextNode("44")
    bndbox.appendChild(xmin)
    xmin.appendChild(xmin_text)
    bndbox.appendChild(ymin)
    ymin.appendChild(ymin_text)
    bndbox.appendChild(xmax)
    xmax.appendChild(xmax_text)
    bndbox.appendChild(ymax)
    ymax.appendChild(ymax_text)
    object1.appendChild(bndbox)
    annotation.appendChild(object1)

    fp = open("../xml/"+'%s.xml' %new_txtname , 'w+')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n',encoding='utf-8')
    fp.close()
