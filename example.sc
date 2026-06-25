incluir <stdio.h>


entero mostrar_linea()
{
    imprimir("----------------------------------------\n");

    retornar 0;
}





entero main()
{

    entero i;
    entero numero;
    entero suma;
    entero factorial;


    imprimir("\n");
    imprimir("========================================\n");
    imprimir("       BIENVENIDO A SPANISH C            \n");
    imprimir("========================================\n");
    imprimir("\n");



    imprimir("Iniciando pruebas...\n");
    imprimir("\n");



    mostrar_linea();



    imprimir("PRUEBA 1: Variables\n");

    numero = 10;
    suma = 0;


    imprimir(
        "Numero guardado: %d\n",
        numero
    );


    imprimir(
        "Suma inicial: %d\n",
        suma
    );



    mostrar_linea();





    imprimir("PRUEBA 2: Bucle para\n");


    para(i = 1; i <= 10; i = i + 1)
    {

        suma = suma + i;


        imprimir(
            "Iteracion %d -> suma = %d\n",
            i,
            suma
        );

    }



    imprimir(
        "Suma final: %d\n",
        suma
    );



    mostrar_linea();







    imprimir("PRUEBA 3: Condiciones\n");


    si(suma > 50)
    {

        imprimir(
            "La suma es mayor que 50\n"
        );

    }

    sino
    {

        imprimir(
            "La suma es menor o igual que 50\n"
        );

    }





    si(numero == 10)
    {

        imprimir(
            "Numero correcto\n"
        );

    }

    sino
    {

        imprimir(
            "Numero incorrecto\n"
        );

    }



    mostrar_linea();







    imprimir("PRUEBA 4: Mientras\n");


    numero = 5;


    mientras(numero > 0)
    {

        imprimir(
            "Cuenta regresiva: %d\n",
            numero
        );


        numero = numero - 1;

    }


    imprimir(
        "Despegue!\n"
    );



    mostrar_linea();









    imprimir("PRUEBA 5: Factorial\n");


    numero = 6;
    factorial = 1;


    mientras(numero > 1)
    {

        factorial = factorial * numero;


        imprimir(
            "Multiplicando por %d, resultado %d\n",
            numero,
            factorial
        );


        numero = numero - 1;

    }



    imprimir(
        "Factorial final: %d\n",
        factorial
    );



    mostrar_linea();








    imprimir("PRUEBA 6: Tabla del 5\n");


    para(i = 1; i <= 10; i = i + 1)
    {

        imprimir(
            "5 x %d = %d\n",
            i,
            5 * i
        );

    }



    mostrar_linea();








    imprimir("PRUEBA 7: Muchas cadenas\n");


    imprimir("Hola mundo!\n");
    imprimir("Esto fue escrito en SpanishC\n");
    imprimir("Traducido automaticamente a C\n");
    imprimir("Compilado usando GCC\n");



    mostrar_linea();








    imprimir("PRUEBA 8: Valores pares\n");


    para(i = 0; i <= 20; i = i + 1)
    {

        si(i % 2 == 0)
        {

            imprimir(
                "%d es par\n",
                i
            );

        }

    }




    mostrar_linea();







    imprimir("PRUEBA 9: Final\n");


    imprimir(
        "Todas las pruebas terminaron correctamente!\n"
    );


    imprimir(
        "SpanishC funciona :)\n"
    );


    imprimir("\n");
    imprimir("========================================\n");


    retornar 0;
}
