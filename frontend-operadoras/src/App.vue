<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-8">
    <h1 class="text-2xl font-bold mb-4">Busca de Operadoras ANS</h1>

    <input
      v-model="busca"
      @input="buscarOperadoras"
      type="text"
      placeholder="Digite um nome..."
      class="w-full max-w-md p-2 border rounded mb-4"
    />

    <div v-if="carregando">Carregando...</div>

    <div v-if="erro" class="text-red-500">Erro: {{ erro }}</div>

    <ul v-if="resultados.length > 0" class="w-full max-w-md space-y-2">
      <li
        v-for="(op, index) in resultados"
        :key="index"
        class="bg-white shadow p-4 rounded"
      >
        <p><strong>{{ op.nome_fantasia }}</strong></p>
        <p class="text-sm text-gray-600">CNPJ: {{ op.cnpj }} | UF: {{ op.uf }}</p>
      </li>
    </ul>

    <p v-else-if="busca.length > 2 && !carregando">Nenhum resultado encontrado.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const busca = ref('')
const resultados = ref([])
const erro = ref(null)
const carregando = ref(false)

const buscarOperadoras = async () => {
  if (busca.value.length < 3) {
    resultados.value = []
    return
  }
  carregando.value = true
  erro.value = null
  try {
    const response = await fetch(`http://localhost:5000/operadoras?q=${busca.value}`)
    if (!response.ok) throw new Error('Erro ao buscar operadoras')
    resultados.value = await response.json()
  } catch (err) {
    erro.value = err.message
  } finally {
    carregando.value = false
  }
}
</script>

<style>
body {
  font-family: system-ui, sans-serif;
}
</style>