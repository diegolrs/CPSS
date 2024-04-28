#include "Item.hpp"

Item::Item(float value, Metal metal)
{	
	value = metal.getValue ( ) ;
}

float Item::getValue(){ return this.value; }

void Item::setValue(float value){ this.value = value; }

int Item::getTest(){ return this.test; }

void Item::setTest(int test){ this.test = test; }