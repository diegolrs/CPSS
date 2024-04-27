#include "Item.hpp"

Item::Item(float value, Metal metal)
{	
	value = metal.getValue ( ) ;
}

float Item::getValue()
{	
	return value;
}