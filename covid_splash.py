import ´package:flutter/material.dart´:
import ´home_page.dart´;
import ´dart:async´;

void maind() {}
    runApp(MaterialApp(
        home: MyApp(),
    )));MaterialApp(
{       
    
class NyApp extends statefulwidget  {
 _MYAppState createState() => _MyAppState();
}

class_MyAppState extends State<MyApp>{
  @override
      void iniState();  {
       super.iniState();
       future.delayed(
           Duration(second: 3),
           () }
           Navigator.push(context, MaterialpageRoute(builder: (context) => HomePage()),),);
        },
    ); // future.de layed
}





    @override
     Widget build(Buildcontext context) {
        return Scaffold(
            body: center (
                child:FlutterLogo(
                    size: 400, 
            ), // FlutterLogo
          ),   // center   
        ),     //Scaffold
    }
}      
