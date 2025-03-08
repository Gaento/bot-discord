# **Configuração Inicial**

## **Importação de Bibliotecas**
- **discord**: Para interagir com a API do Discord.
- **commands**: Para criar comandos personalizados para o bot.
- **youtube_search** e **spotipy**: Para buscar músicas no YouTube e Spotify.

## **Configuração do Bot**
- Define o prefixo dos comandos (.).
- Ativa as intents (discord.Intents.all()) para permitir eventos como on_member_join().
- Configura a API do Spotify (spotipy.Spotify), usando credenciais obtidas no **Spotify Developer Dashboard**.

# **Eventos Especiais**

## **✅ Quando o Bot Inicia (on_ready)**
Quando o bot estiver pronto, ele exibe a mensagem:


## **✅ Quando um Membro Entra no Servidor (on_member_join)**
- Obtém informações do usuário (avatar, nome e ID).
- Envia uma mensagem de boas-vindas com um embed contendo:
  - Nome e avatar do usuário.
  - Mensagem personalizada: "Timor est quod patimur, finiendus est. 🐀"
  - Imagem (olho.gif).

# **Comandos Disponíveis**

## **✅ .clear (Limpar Mensagens)**
- Exclui um número de mensagens no chat (padrão: 10).
- Somente usuários com permissão **"Gerenciar Mensagens"** podem usá-lo.

## **✅ .ajuda (Lista de Comandos)**
- Exibe um embed com a lista de comandos disponíveis.

## **✅ .youtube <música> (Buscar no YouTube)**
- O usuário digita:
- O bot busca no YouTube e responde com o link do vídeo.

## **✅ .spotify <música> (Buscar no Spotify)**
- O usuário digita:
- O bot busca no Spotify e responde com o link da música.

## **Rodando o Bot**
No final do código, temos:


## **bot.run('SEU_TOKEN_DISCORD')**

**☝ Essa linha inicia o bot e o conecta ao Discord usando o TOKEN da API.**

# **🚀 Resumindo**
**O bot pode:**

- ✅ **Enviar mensagens automáticas.**
- ✅ **Limpar mensagens do chat.**
- ✅ **Buscar músicas no YouTube e Spotify.**
- ✅ **Exibir uma lista de comandos.**
