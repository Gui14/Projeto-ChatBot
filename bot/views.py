from django.shortcuts import render, redirect
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from .models import conversa
from django.contrib.auth.decorators import login_required
from usuarios.models import info_cadastro
import re

from django.shortcuts import render
from chatterbot import ChatBot

from django.shortcuts import render
from chatterbot import ChatBot

from django.shortcuts import render
from chatterbot import ChatBot

from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.conversation import Statement

def aila(request):
    chatbot = ChatBot("Aila")    
    pergunta =[]
    resposta = []

    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'aila.html')
        elif request.method == 'POST':
            pergunta_digitada = request.POST.get('pergunta')
            resposta_digitada = chatbot.get_response(pergunta_digitada)
            
            
            pergunta.append(pergunta_digitada)
            resposta.append(resposta_digitada)
            # conversas = conversa(
            #     pergunta=pergunta_digitada,
            #     resposta=resposta_digitada
            # )
            # conversas.save()

            # dialogo = conversa.objects.all()
            # delete = conversa.objects.all()

            # if pergunta_digitada == 'deletar':
            #     delete.delete()
            return render(request, 'aila.html', {'pergunta': pergunta, 'resposta':resposta})
            # {'conversas':dialogo}
    else:
        return HttpResponse('Você não pode acessar essa página, faça primeiro o login')
    



def inicio(request):

    def remover_formatacao_telefone(numero):
        # Use uma expressão regular para encontrar apenas os dígitos
        numero_limpo = re.sub(r'\D', '', numero)
        return numero_limpo

    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'index.html')
        else:
            usuario = info_cadastro.objects.get(email= request.user)
            mensagem = f'Estou em perigo! Segue a minha localização {usuario.endereco} bairro: {usuario.bairro}'
            telefone = remover_formatacao_telefone(usuario.telefone_guardiao)
            url_whatsapp = f"https://api.whatsapp.com/send?phone={telefone}&text={mensagem}"
            return redirect(url_whatsapp)
    else:
         if request.method == "GET":
            return render(request, 'index2.html')
    

def faq(request):
    def remover_formatacao_telefone(numero):
        numero_limpo = re.sub(r'\D', '', numero)
        return numero_limpo

    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'faq.html')
        else:
            usuario = info_cadastro.objects.get(email= request.user)
            mensagem = 'Olá, está é uma mensagem programada'
            telefone = remover_formatacao_telefone(usuario.telefone_guardiao)
            url_whatsapp = f"https://api.whatsapp.com/send?phone={telefone}&text={mensagem}"
            return redirect(url_whatsapp)
    else:
         if request.method == "GET":
            return render(request, 'faq2.html')
    
# conversa = [
        #     'Oi?', 
        #     'Eae, tudo certo?',
        #     'Qual o seu nome?', 
        #     'Aila, sua amiga bot',
        #     'Por que seu nome é Aila?', 
        #     'Porque sim',
        #     'Prazer em te conhecer', 
        #     'Igualmente meu querido',
        #     'Quantos anos você tem?', 
        #     'Eu nasci dia 23 de agosto de 2023, faz as contas, rs.',
        #     'Você gosta de videogame?', 
        #     'Eu sou um bot, eu só apelo.',
        #     'Qual a capital da Islândia?', 
        #     'Reikjavik, lá é muito bonito.',
        #     'Qual o seu personagem favorito?', 
        #     'Gandalf, o mago.',
        #     'Qual a sua bebida favorita?', 
        #     'Eu bebo café, o motor de todos os programas de computador.',
        #     'Qual o seu gênero?', 
        #     'Sou um chatbot e gosto de algoritmos',
        #     'Hahahaha', 'kkkk',
        #     'kkk', 'kkkk',
        #     'Conhece a Siri?', 'Conheço, mas nunca fui com a cara.',
        #     'Conhece a Alexa?', 'MINHA BESTTT',
        #     'O que é violência contra a mulher?','A violência contra a mulher é qualquer ação ou conduta que cause dano físico, sexual, psicológico ou patrimonial a uma mulher, com base no gênero. Isso inclui agressões, abuso verbal, assédio sexual, controle financeiro e outras formas de violência.',
        #     'Quais são os tipos de violência reconhecidos pela Lei Maria da Penha?', 'A Lei Maria da Penha reconhece cinco tipos de violência contra a mulher: violência física, violência psicológica, violência sexual, violência patrimonial e violência moral.',
        #     'O que é a Lei Maria da Penha?', 'A Lei Maria da Penha é uma legislação brasileira criada para combater a violência doméstica e familiar contra a mulher. Ela estabelece medidas protetivas, penas mais severas para agressores e promove a criação de serviços de apoio às vítimas.',
        #     'Como posso denunciar um caso de violência contra a mulher?', ' Você pode denunciar casos de violência contra a mulher ligando para o número 180, que é a Central de Atendimento à Mulher. Além disso, você pode procurar uma Delegacia Especializada de Atendimento à Mulher (DEAM) mais próxima para fazer a denúncia pessoalmente.',
        #     'O que são medidas protetivas?', 'Medidas protetivas são ordens judiciais emitidas pelo juiz para proteger a mulher vítima de violência. Elas podem incluir o afastamento do agressor, proibição de contato e outras medidas para garantir a segurança da vítima.',
        #     'Como a Defensoria Pública pode me ajudar em caso de violência?', 'A Defensoria Pública oferece assistência jurídica gratuita para mulheres que não têm recursos para contratar um advogado. Eles podem ajudá-la a obter medidas protetivas, orientá-la sobre seus direitos e representá-la legalmente.',
        #     'O que é a Casa da Mulher Brasileira?', 'A Casa da Mulher Brasileira é um espaço que oferece diversos serviços de apoio às mulheres vítimas de violência, incluindo atendimento psicossocial, orientação jurídica, abrigo temporário e outras formas de suporte',
        #     'O que devo fazer se estiver em perigo iminente?', 'Em caso de perigo iminente, ligue imediatamente para a polícia no número 190. Sua segurança é a prioridade, e as autoridades estão preparadas para responder a situações de emergência.',
        #     'Como posso reconhecer sinais de violência doméstica?', 'Alguns sinais de violência doméstica podem incluir hematomas inexplicáveis, mudanças de comportamento, isolamento social, medo do parceiro, entre outros. Se você ou alguém que você conhece está passando por isso, é importante buscar ajuda.',
        #     'Existe algum serviço de apoio psicológico para vítimas de violência?', 'Sim, muitos centros de atendimento à mulher oferecem apoio psicológico gratuito para vítimas de violência. Você pode procurar ajuda em uma Delegacia Especializada ou na Casa da Mulher Brasileira.',
        #     'Quais são os direitos das mulheres em um relacionamento abusivo?', 'As mulheres têm o direito de viver em um ambiente seguro e livre de violência. Elas também têm o direito de buscar ajuda, obter medidas protetivas e denunciar o agressor.',
        #     'O que é o Disque 100?', 'O Disque 100 é um serviço de denúncia de violações de direitos humanos, incluindo a violência contra a mulher. Você pode ligar para o número 100 para denunciar casos de abuso e maus-tratos.',
        #     'Quais são as consequências legais para os agressores de violência contra a mulher?', 'Os agressores podem enfrentar consequências legais, que variam de acordo com a gravidade do crime. Isso pode incluir prisão, pagamento de multas e ordens de restrição.',
        #     'O que fazer se eu não tiver recursos financeiros para sair de um relacionamento abusivo?', 'Existem organizações e abrigos que podem fornecer abrigo temporário e assistência para mulheres em situações de violência. Você pode procurar ajuda em uma DEAM ou na Casa da Mulher Brasileira',
        #     'Como posso apoiar uma amiga que está em um relacionamento abusivo?','Você pode oferecer apoio emocional, encorajar sua amiga a buscar ajuda profissional, ajudá-la a criar um plano de segurança e não julgá-la por sua situação.',
        #     'O que é o Plano Nacional de Políticas para as Mulheres?', 'O Plano Nacional de Políticas para as Mulheres é uma iniciativa do governo brasileiro que visa promover a igualdade de gênero e combater a violência contra a mulher por meio de políticas públicas específicas.'
        # ]
        # trainer = ListTrainer(chatbot)
        # trainer.train(conversa)