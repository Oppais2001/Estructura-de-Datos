import 'dart:io';
import 'dart:math';
void main(){
  List<int>Lista1=[];
  List<int>Lista2=[];
  List<int>Lista3=[];
  List<int>Lista4=[];
  var random=Random();
  for(int i=0;i<10;i++){
    int NumeroAleatorio=random.nextInt(10)+10;
    int NumeroAleatorio1=random.nextInt(10)+10;
    Lista1.add(NumeroAleatorio);
    Lista2.add(NumeroAleatorio1);
  }
  for(int j=0;j<5;j++){
    print("ingrese valor para la lista:");
    int NumeroIngresado=int.parse(stdin.readLineSync()!);
    Lista3.add(NumeroIngresado);
  }
  print("Lista 1:");
  print(Lista1);
  print("Lista 2:");
  print(Lista2);
  print("Lista 3:");
  print(Lista3);
  print("Lista concatenada");
  Lista4=Lista1+Lista2+Lista3;
  print(Lista4);
  int Promedio=0;
  for(int k=0;k<25;k++){
    int NumPromedio;
    NumPromedio=Lista4[k];
    Promedio+=NumPromedio;
  }
  print("Promedio de la lista concatenada:");
  print(Promedio/25);
  Lista4.sort();
  Lista4.reversed.toList();
  print("Lista ordenada de forma ascendente:");
  print(Lista4);
}