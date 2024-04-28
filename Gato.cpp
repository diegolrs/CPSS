#include "Gato.hpp"

std::string Gato::FazSom()
{	
	return "Miau";
}

std::string Gato::getNome(){ return this->nome; }

void Gato::setNome(std::string nome){ this->nome = nome; }

int Gato::getIdade(){ return this->idade; }

void Gato::setIdade(int idade){ this->idade = idade; }

Cor Gato::getCor(){ return this->cor; }

void Gato::setCor(Cor cor){ this->cor = cor; }