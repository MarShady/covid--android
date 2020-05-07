import ´ package:flutter/material.dart´;

class HomePage extendes stateleswidget {
    @override
    widget build (BuildContext context) {
        return Scaffold(
     body: center(
         child: Text("Maria shaday  ),
     )   
    }
}
routes:<string,widgetBuilder>{
    "/inicio":(BuildContext context)=>analisis de foto o imagen(),
}
onPressed:() {
    Navigator.pushNmaed(context, "/analisis de foto o imagen");
},

