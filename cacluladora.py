#!/usr/bin/env python3
"""Calculadora estándar (CLI).

Soporta: suma, resta, multiplicación, división, potencia, raíz cuadrada y módulo.
Modo interactivo y un modo `--demo` para pruebas rápidas.
"""
import math
import argparse
import sys


def add(a: float, b: float) -> float:
    return a + b


def sub(a: float, b: float) -> float:
    return a - b


def mul(a: float, b: float) -> float:
    return a * b


def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


def sqrt(a: float) -> float:
    if a < 0:
        raise ValueError("Raíz de número negativo")
    return math.sqrt(a)


def mod(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Módulo por cero")
    return a % b


def menu() -> None:
    print("Calculadora estándar")
    print("Operaciones disponibles:")
    print(" 1) Suma")
    print(" 2) Resta")
    print(" 3) Multiplicación")
    print(" 4) División")
    print(" 5) Potencia (a^b)")
    print(" 6) Raíz cuadrada")
    print(" 7) Módulo")
    print(" 0) Salir")


def prompt_number(prompt: str) -> float:
    while True:
        try:
            val = input(prompt)
            return float(val)
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")


def interactive_loop() -> None:
    menu()
    while True:
        choice = input("Seleccione operación (0-7): ").strip()
        if choice == "0":
            print("Saliendo.")
            return
        try:
            if choice == "1":
                a = prompt_number("a = ")
                b = prompt_number("b = ")
                print("Resultado:", add(a, b))
            elif choice == "2":
                a = prompt_number("a = ")
                b = prompt_number("b = ")
                print("Resultado:", sub(a, b))
            elif choice == "3":
                a = prompt_number("a = ")
                b = prompt_number("b = ")
                print("Resultado:", mul(a, b))
            elif choice == "4":
                a = prompt_number("a = ")
                b = prompt_number("b = ")
                print("Resultado:", div(a, b))
            elif choice == "5":
                a = prompt_number("a = ")
                b = prompt_number("b = ")
                print("Resultado:", power(a, b))
            elif choice == "6":
                a = prompt_number("a = ")
                print("Resultado:", sqrt(a))
            elif choice == "7":
                a = prompt_number("a = ")
                b = prompt_number("b = ")
                print("Resultado:", mod(a, b))
            else:
                print("Opción no reconocida.")
        except Exception as e:
            print("Error:", e)


def run_demo() -> None:
    # Pruebas simples impresas para verificar funcionalidad
    print("Demo: comprobando operaciones básicas...")
    tests = [
        (add, (2, 3), 5),
        (sub, (5, 2), 3),
        (mul, (3, 4), 12),
        (div, (10, 2), 5),
        (power, (2, 8), 256),
        (sqrt, (16,), 4),
        (mod, (10, 3), 1),
    ]
    all_ok = True
    for fn, args, expected in tests:
        result = fn(*args)
        ok = math.isclose(result, expected, rel_tol=1e-9)
        status = "OK" if ok else "FAIL"
        print(f"{fn.__name__}{args} -> {result} (esperado {expected}) [{status}]")
        if not ok:
            all_ok = False
    if all_ok:
        print("Todas las pruebas pasaron.")
    else:
        print("Algunas pruebas fallaron.")


def parse_args():
    p = argparse.ArgumentParser(description="Calculadora estándar (CLI)")
    p.add_argument("--demo", action="store_true", help="Ejecutar demostración y salir")
    return p.parse_args()


def main():
    args = parse_args()
    if args.demo:
        run_demo()
        return
    try:
        interactive_loop()
    except (KeyboardInterrupt, EOFError):
        print("\\nSaliendo.")


if __name__ == "__main__":
    main()