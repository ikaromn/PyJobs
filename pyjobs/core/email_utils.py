def empresa_cadastrou_vaga(empresa, vaga):
    return """
Olá {empresa},

Aproveite e ajude o PyJobs a se manter online doando através do: https://apoia.se/pyjobs

Agora que você criou a vaga {vaga}, nós lhe enviaremos os detalhes de quem se inscreveu para ela, assim você conseguirá\
 entrar em contato com eles

Em breve iremos lhe enviar o link da sua vaga para divulgação!

Abraços,
Vinicius Mesel
@vmesel
Doe em: http://apoia.se/pyjobs
""".format(empresa=empresa, vaga=vaga)

def vaga_publicada(empresa, vaga, pk):
    return """
Olá {empresa},

Aproveite e ajude o PyJobs a se manter online doando através do: https://apoia.se/pyjobs

Agora a vaga {vaga} foi avaliada por nossos colaboradores e foi publicada!

Para acessar a sua vaga, entre no link: http://www.pyjobs.com.br/job/{pk}/

Abraços,
Vinicius Mesel
@vmesel
Doe em: http://apoia.se/pyjobs
""".format(empresa=empresa, vaga=vaga, pk=pk)


def contato_cadastrado_empresa(pessoa, vaga):
    return """
    Olá,

    Aproveite e ajude o PyJobs a se manter online doando através do: https://apoia.se/pyjobs

    Você recebeu uma nova pessoa interessada em sua vaga: {vaga}

    Nome do interessado(a): {nome}
    Email do interessado(a): {email}
    Telefone do interessado(a): {telefone}
    Linkedin do interessado(a): {linkedin}
    GitHub do interessado(a): {github}
    Portfolio do interessado(a): {portfolio}

    Estamos lhe enviando este email para te avisar que a pessoa está interessada em sua vaga e aguarda uma resposta!

    Em breve, nós lhe contataremos com mais interessados!

    Para acessar o PyJobs, entre no link: http://www.pyjobs.com.br

    Abraços,
    Vinicius Mesel
    @vmesel
    Doe em: http://apoia.se/pyjobs
    """.format(
    nome=pessoa.get_full_name(),
    vaga=vaga,
    email=pessoa.email,
    telefone=pessoa.profile.cellphone,
    portfolio=pessoa.profile.portfolio,
    github=pessoa.profile.github,
    linkedin=pessoa.profile.linkedin
    )

def contato_cadastrado_pessoa(pessoa, vaga):
        return """
Olá {nome},

Recebemos seu interesse na oportunidade: {vaga}

Aproveite e ajude o PyJobs a se manter online doando através do: https://apoia.se/pyjobs

Estamos lhe enviando este email para te avisar que a empresa responsável pela sua vaga recebeu seus dados e em breve,\
 eles entrarão em contato com você!

Em breve, nós lhe contataremos com mais informações sobre a vaga!

Para acessar o PyJobs, entre no link: http://www.pyjobs.com.br

Abraços,
Vinicius Mesel
@vmesel
Doe em: http://apoia.se/pyjobs
""".format(nome=pessoa.get_full_name(), vaga=vaga)


def contact_email(name, email, subject, message):
    return """
Olá PyJobs,

A pessoa: {name} quer falar sobre {subject}.

A mensagem dela é:

{message}

Para mandar um email para ela, basta enviar para: {email}
    """.format(name=name, email=email, subject=subject, message=message)
