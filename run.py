#!./venv/bin/python
#
#
#
#
import app

def main():
    print('Hi')
    a = app.Product( )
    a.name = 'product 1'
    a.save()

if __name__ == '__main__':
    main()
