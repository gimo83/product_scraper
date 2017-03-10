#!./venv/bin/python
#
#
#
#
import app

def main():
    print('Creating products:',end=" "),
    for x in range(10):
        a = app.Product( )
        a['name'] = 'product '+ str(x)
        a.save()
        print('.',end="")
    print(" Done")

if __name__ == '__main__':
    main()
