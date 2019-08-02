from pocketsphinx import pocketsphinx, Jsgf, FsgModel
import os

model_path = "/Users/xrickliao/.local/share/virtualenvs/pyspeechrecog-Pbkb6zQf/lib/python3.6/site-packages/speech_recognition/pocketsphinx-data/"

language = 'zh-CN'
grammar_file = 'speechcommand2'

#grammar_path = os.path.join(modelPath, language, grammar_file)
try:
    grammar_abspath = os.path.abspath(os.path.dirname(grammar_file))
    grammar_full_name = os.path.splitext(os.path.basename(grammar_file))
    grammar_name = grammar_full_name[0]#os.path.splitext(os.path.basename(grammar_file))[0]
    grammar_path = os.path.join(grammar_abspath,grammar_file)
    fsg_path = "{0}/{1}.fsg".format(grammar_abspath, grammar_name)
    print("abspath: ",grammar_abspath)
    print("grammar_full_name: ", grammar_full_name)
    print("grammar_name: ", grammar_name)
    print("grammar_path: ", grammar_path)
    print("fsg_path: ", fsg_path)
    #print("pocketsphinx.get_model_path():{}".format(pocketsphinx.get_model_path()))
    # Create decoder object
    config = pocketsphinx.Decoder.default_config()
    config.set_string("-hmm", os.path.join(model_path, language, 'acoustic-model'))
    config.set_string("-lm", os.path.join(model_path,language, 'language-model.lm.bin'))
    config.set_string("-dict", os.path.join(model_path, language,'pronounciation-dictionary.dict'))
    #config.set_string("-logfn", os.devnull)
    decoder = pocketsphinx.Decoder(config)

    if decoder:
        print("decoder is created")


    jsgf = Jsgf(grammar_path)
    if jsgf :
        print("jsgf object is created.")
        rule_string = "{0}.{0}".format(grammar_name)
        print(rule_string)
        rule = jsgf.get_rule(rule_string)
        print(rule)
        fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
        fsg.writefile(fsg_path)

    
    #fsg = FsgModel("speechcommand.fsg", decoder.get_logmath(), 7.5)

    print("Grammar Filepath: {}".format(grammar_path))
    print("Grammar FileName: {}".format(grammar_name))
    print(".fsg path: {}".format(fsg_path))
    decoder.set_fsg(grammar_file, fsg) #錯誤原因：在發音詞典中「八個」的拼音，拼成：ba，正確是：b a。二個要分開
    #decoder.set_search(grammar_file)
except Exception as e:
    print('Ach no! {0}'.format(e))
finally:
    os.remove('speechcommand2.fsg')  # Remove again to help prove that the grammar to fsg conversion isn't at fault
