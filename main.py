from yacc import parser
import sys

if len(sys.argv) > 1:
    result = None
    try:
        content_file = open(sys.argv[1], 'r')
        result = parser.parse(content_file.read())
        content_file.close()
    except:
        print('Arquivo não encontrado!')


    if result is None: 
        print('Não foi possível decriptar o arquivo!')
    else:
        try:
            result_file = open('result_' + sys.argv[1], 'w')
            result_file.write(result)
            result_file.close()
        except Exception as e:
            print(f'Não foi possível gerar o novo arquivo!')

else:
    while True:
        try:
            input_str = input('file name -> ')
        except EOFError:
            break
        if not input_str: continue

        try:
            content_file = open(input_str, 'r')
            result = parser.parse(content_file.read())
            content_file.close()
        except:
            print('Arquivo não encontrado!')
            continue

        if result is None: 
            print('Não foi possível decriptar o arquivo!')

        try:
            result_file = open('result_' + input_str, 'w')
            result_file.write(result)
            result_file.close()
        except Exception as e:
            print(f'Não foi possível gerar o novo arquivo!')
