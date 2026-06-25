"""Tokenizer utilities for Spanish-C source code.

This module can scan code and return all Spanish-C keywords found,
while ignoring keywords that appear in comments and string/char literals.
"""

from __future__ import annotations

from dataclasses import dataclass


SPANISH_C_KEYWORDS = {
	# Types
	"vacio",
	"entero",
	"caracter",
	"flotante",
	"doble",
	"largo",
	"corto",
	"firmado",
	"sin_signo",
	# Control flow
	"si",
	"sino",
	"mientras",
	"hacer",
	"para",
	"retornar",
	"romper",
	"continuar",
	# Switch
	"seleccionar",
	"caso",
	"predeterminado",
	# Storage classes
	"automatico",
	"registro",
	"estatico",
	"externo",
	# Qualifiers and misc
	"constante",
	"volatil",
	"restringido",
	"en_linea",
	# Compound types
	"estructura",
	"union",
	"enumeracion",
	"typedef",
	# Boolean and null-like
	"verdadero",
	"falso",
	"nulo",
	# C11/C23 keywords
	"alinear",
	"alineacion",
	"atomo",
	"sin_retorno",
	"estatico_assert",
	"hilo_local",
	# Preprocessor-like words
	"incluir",
	"definir",
	"si_definido",
	"si_no_definido",
	"fin_si",
	"advertencia",
	"error",
}


@dataclass(frozen=True)
class Token:
	value: str
	start: int
	end: int


def _is_ident_start(ch: str) -> bool:
	return ch.isalpha() or ch == "_"


def _is_ident_part(ch: str) -> bool:
	return ch.isalnum() or ch == "_"


def extract_spanish_keywords(code: str) -> list[str]:
	"""Return Spanish-C keywords found in order of appearance.

	Repeated keywords are included each time they appear in code.
	"""

	return [token.value for token in tokenize_spanish_keywords(code)]


def tokenize_spanish_keywords(code: str) -> list[Token]:
	"""Tokenize and return Spanish-C keyword tokens from source code.

	The scanner ignores keywords that appear inside:
	- single-line comments: // ...
	- block comments: /* ... */
	- string literals: "..."
	- char literals: '...'
	"""

	tokens: list[Token] = []
	i = 0
	n = len(code)

	while i < n:
		ch = code[i]

		# Skip single-line comments.
		if ch == "/" and i + 1 < n and code[i + 1] == "/":
			i += 2
			while i < n and code[i] != "\n":
				i += 1
			continue

		# Skip block comments.
		if ch == "/" and i + 1 < n and code[i + 1] == "*":
			i += 2
			while i + 1 < n and not (code[i] == "*" and code[i + 1] == "/"):
				i += 1
			i = i + 2 if i + 1 < n else n
			continue

		# Skip string literals.
		if ch == '"':
			i += 1
			while i < n:
				if code[i] == "\\":
					i += 2
					continue
				if code[i] == '"':
					i += 1
					break
				i += 1
			continue

		# Skip char literals.
		if ch == "'":
			i += 1
			while i < n:
				if code[i] == "\\":
					i += 2
					continue
				if code[i] == "'":
					i += 1
					break
				i += 1
			continue

		if _is_ident_start(ch):
			start = i
			i += 1
			while i < n and _is_ident_part(code[i]):
				i += 1

			ident = code[start:i]
			if ident in SPANISH_C_KEYWORDS:
				tokens.append(Token(value=ident, start=start, end=i))
			continue

		i += 1

	return tokens


if __name__ == "__main__":
	sample = """
entero principal() {
	// si should be ignored here
	si (verdadero) {
		retornar 0;
	}
}
"""
	print(extract_spanish_keywords(sample))
