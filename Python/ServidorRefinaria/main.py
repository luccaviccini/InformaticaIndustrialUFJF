from servidormodbus import ServidorMODBUS


s = ServidorMODBUS('localhost',502)
s.run()

if __name__ == '__main__':
    main()