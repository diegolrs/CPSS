#pragma once
#include "Animal"
#include <string>

class Gato : Animal
{
    private:
        std::string nome;
        int idade;
        Cor cor;
    public:
        std::string FazSom();
	public:
		std::string getNome();
		void setNome(std::string nome);
		int getIdade();
		void setIdade(int idade);
		Cor getCor();
		void setCor(Cor cor);
};