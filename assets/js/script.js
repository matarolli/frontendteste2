// script.js

// Mensagem de confirmação de carregamento (opcional)
console.log('Script.js carregado com sucesso');

// Inicialização do Smooth Scroll
var scroll = new SmoothScroll('a[href*="#"]', {
    speed: 800,
    speedAsDuration: true
});

// Dados das classes
var classes = [
    {
        nome: 'Bárbaro',
        imagem: 'assets/img/d4barbaro.webp',
        descricao: 'O Bárbaro é um guerreiro corpulento e impetuoso...'
    },
    {
        nome: 'Druida',
        imagem: 'assets/img/d4druida.webp',
        descricao: 'O Druida é um mestre da natureza...'
    },
    {
        nome: 'Necromancer',
        imagem: 'assets/img/d4necro.webp',
        descricao: 'O Necromancer manipula as forças da vida e da morte...'
    },
    {
        nome: 'Renegado',
        imagem: 'assets/img/d4rogue.webp',
        descricao: 'O Renegado é um combatente ágil e versátil...'
    },
    {
        nome: 'Feiticeiro',
        imagem: 'assets/img/d4sorcerer.webp',
        descricao: 'O Feiticeiro domina as artes arcanas...'
    },
    {
        nome: 'Spiritborn',
        imagem: 'assets/img/d4spirit.webp',
        descricao: 'O Spiritborn é um ser místico conectado ao mundo espiritual...'
    }
];

// Seleciona todos os botões das classes
var botoesClasses = document.querySelectorAll('.btn-classe');

// Seleciona os elementos que serão atualizados
var nomeClasse = document.querySelector('#descricao-classe h3');
var imagemClasse = document.querySelector('#descricao-classe .conteudo-classe img');
var descricaoClasse = document.querySelector('#descricao-classe .conteudo-classe p');

// Adiciona o event listener a cada botão
botoesClasses.forEach(function(botao) {
    botao.addEventListener('click', function() {
        // Obtém o índice da classe clicada
        var index = botao.getAttribute('data-index');
        var classeSelecionada = classes[index];

        // Verifica se a classe selecionada existe
        if (classeSelecionada) {
            // Atualiza o conteúdo dinâmico
            nomeClasse.textContent = classeSelecionada.nome;
            imagemClasse.src = classeSelecionada.imagem;
            imagemClasse.alt = classeSelecionada.nome;
            descricaoClasse.textContent = classeSelecionada.descricao;

            // Atualiza a classe 'active' nos botões
            botoesClasses.forEach(function(btn) {
                btn.classList.remove('active');
            });
            botao.classList.add('active');
        } else {
            console.error('Classe não encontrada no índice:', index);
        }
    });
});
