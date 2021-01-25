def even_index_number(our_str):
    for i in range(0 ,len(our_str) ,2):
        print ( our_str[i] )

our_str = input ("What 's your str ?  ")
print ( "Orginal String is {}".format (our_str) ) 
print ( "Printing only even index chars" )

even_index_number ( our_str )
