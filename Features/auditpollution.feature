#language: pt
Funcionalidade: Poluir auditoria
   
   '''Eu como usuário quero poluir os registros de auditoria'''

      Cenario: Poluir a auditoria
      Dado acesso o D-Guard Cloud
      Quando faço o meu login
      E começo a gerar várias auditorias de acesso as câmeras
      Então eu polui a auditoria
