import 'dart:math';
void main(){
  Random random=Random();
  List<int> lista1=[];
  List<int> lista2=[];
  List<int> lista3=[];
  List<double> promedios=[0,0,0];
  for(int i=0; i<7;i++){
    int aleatorio1=30+random.nextInt(71);
    int aleatorio2=30+random.nextInt(71);
    int aleatorio3=30+random.nextInt(71);
    lista1.add(aleatorio1);
    lista2.add(aleatorio2);
    lista3.add(aleatorio3);
    double promedio1 = aleatorio1 / 7;
    double promedio2 = aleatorio2 / 7;
    double promedio3 = aleatorio3 / 7;
    promedios[0]+=promedio1;
    promedios[1]+=promedio2;
    promedios[2]+=promedio3;
  }
  print('Lista 1:');
  print(lista1);
  print('Lista 2:');
  print(lista2);
  print('Lista 3:');
  print(lista3);
  print('lista promedios:');
  print(promedios);
}