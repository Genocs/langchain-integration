<!-- PROJECT SHIELDS -->
[![License][license-shield]][license-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Discord][discord-shield]][discord-url]
[![Gitter][gitter-shield]][gitter-url]
[![Twitter][twitter-shield]][twitter-url]
[![Twitterx][twitterx-shield]][twitterx-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[license-shield]: https://img.shields.io/github/license/Genocs/langchain-integration?color=2da44e&style=flat-square
[license-url]: https://github.com/Genocs/langchain-integration/blob/main/LICENSE
[contributors-shield]: https://img.shields.io/github/contributors/Genocs/langchain-integration.svg?style=flat-square
[contributors-url]: https://github.com/Genocs/langchain-integration/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Genocs/langchain-integration?style=flat-square
[forks-url]: https://github.com/Genocs/langchain-integration/network/members
[stars-shield]: https://img.shields.io/github/stars/Genocs/langchain-integration.svg?style=flat-square
[stars-url]: https://img.shields.io/github/stars/Genocs/langchain-integration?style=flat-square
[issues-shield]: https://img.shields.io/github/issues/Genocs/langchain-integration?style=flat-square
[issues-url]: https://github.com/Genocs/langchain-integration/issues
[discord-shield]: https://img.shields.io/discord/1106846706512953385?color=%237289da&label=Discord&logo=discord&logoColor=%237289da&style=flat-square
[discord-url]: https://discord.com/invite/fWwArnkV
[gitter-shield]: https://img.shields.io/badge/chat-on%20gitter-blue.svg
[gitter-url]: https://gitter.im/genocs/
[twitter-shield]: https://img.shields.io/twitter/follow/genocs?color=1DA1F2&label=Twitter&logo=Twitter&style=flat-square
[twitter-url]: https://twitter.com/genocs
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/giovanni-emanuele-nocco-b31a5169/
[twitterx-shield]: https://img.shields.io/twitter/url/https/twitter.com/genocs.svg?style=social
[twitterx-url]: https://twitter.com/genocs


<p align="center">
    <img src="./assets/genocs-library-logo.png" alt="icon">
</p>


# Langchain Integration

Before run any python files install the packages

```bash
pip install -r ./src/requirements.txt
```

Then set the environment variables

```bash
set OPENAI_API_KEY=<your_api_key>
set AMQP_URL=<your_rabbitmq_connection_string>
```
Alternativly you can use .env file.

.env file example:

``` bash
# Open AI configuration
OPENAI_API_KEY=<<YOUR_API_KEY>>

# MongoDB configuration
MONGODB_CONNECTION_STRING=mongodb://localhost:27017

# RabbitMQ configuration
RABBITMQ_CONNECTION_NAME=my_connection
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USERNAME=guest
RABBITMQ_PASSWORD=guest
RABBITMQ_VHOST=/
RABBITMQ_QUEUE_NAME=my_queue

# Fiscanner configuration
FISCANNER_URL=https://fiscanner-platform.azurewebsites.net
``` 

## Run with python

```bash
python.exe ./src/main.py
```

## Run with chainlit

Install chainlit

```bash
pip install chainlit
```

If you are using conda, you can install it with

```bash
conda install -c conda-forge chainlit
```

Or you can install chainlit with pip

```bash
pip install chainlit
```

To test if chanlit is installed correctly run:

```bash
chainlit hello
```

Then run chainlit application

```bash
chainlit run ./src/07_langchain_chainlit.py
```


## License

This project is licensed with the [MIT license](LICENSE).

## Changelogs

View Complete [Changelogs](https://github.com/Genocs/microservice-template/blob/main/CHANGELOGS.md).

## Community

- Discord [@genocs](https://discord.com/invite/fWwArnkV)
- Facebook Page [@genocs](https://facebook.com/Genocs)
- Youtube Channel [@genocs](https://youtube.com/c/genocs)


## Support

Has this Project helped you learn something New? or Helped you at work?
Here are a few ways by which you can support.

- ⭐ Leave a star! 
- 🥇 Recommend this project to your colleagues.
- 🦸 Do consider endorsing me on LinkedIn for ASP.NET Core - [Connect via LinkedIn](https://www.linkedin.com/in/giovanni-emanuele-nocco-b31a5169/) 
- ☕ If you want to support this project in the long run, [consider buying me a coffee](https://www.buymeacoffee.com/genocs)!
  

[![buy-me-a-coffee](https://raw.githubusercontent.com/Genocs/blazor-template/main/assets/buy-me-a-coffee.png "buy-me-a-coffee")](https://www.buymeacoffee.com/genocs)

## Code Contributors

This project exists thanks to all the people who contribute. [Submit your PR and join the team!](CONTRIBUTING.md)

[![genocs contributors](https://contrib.rocks/image?repo=Genocs/blazor-template "genocs contributors")](https://github.com/genocs/blazor-template/graphs/contributors)

## Financial Contributors

Become a financial contributor and help me sustain the project. [Support the Project!](https://opencollective.com/genocs/contribute)

<a href="https://opencollective.com/genocs"><img src="https://opencollective.com/genocs/individuals.svg?width=890"></a>


## Acknowledgements
- [Chainlit](https://github.com/Chainlit/chainlit)
- [Masstransit](https://github.com/MassTransit/MassTransit)