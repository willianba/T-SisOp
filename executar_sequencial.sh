#!/bin/bash
DIR=`pwd`
PATH=tempos_sequencial
cd $DIR/src/java

echo "Compilando código-fonte"
javac *.java

echo "Movendo código-fonte compilado"
mv *.class $DIR/$PATH/
cd $DIR/$PATH/

echo "Realizando execução sequencial"
for i in {0..9};
do
	echo "Execução " $((i+1))
	#java Sequencial > tempo_sequencial_0$i
done

echo "Deletando arquivos compilados"
rm *.class
cd $DIR

echo "Finalizado: tempos de execução sequencial"