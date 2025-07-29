<template>
  <div class="bg-white p-6 rounded-lg shadow-md mb-6">
    <h3 class="text-lg font-semibold text-gray-900 mb-4">Filter Movies</h3>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- Genre Filter -->
      <div>
        <label for="genre" class="block text-sm font-medium text-gray-700 mb-1">
          Genre
        </label>
        <select 
          id="genre" 
          v-model="selectedGenre" 
          @change="updateFilters"
          class="filter-select"
        >
          <option value="">All Genres</option>
          <option v-for="genre in genres" :key="genre.id" :value="genre.id">
            {{ genre.name }}
          </option>
        </select>
      </div>

      <!-- Director Filter -->
      <div>
        <label for="director" class="block text-sm font-medium text-gray-700 mb-1">
          Director
        </label>
        <select 
          id="director" 
          v-model="selectedDirector" 
          @change="updateFilters"
          class="filter-select"
        >
          <option value="">All Directors</option>
          <option v-for="director in directors" :key="director.id" :value="director.id">
            {{ director.name }}
          </option>
        </select>
      </div>

      <!-- Actor Filter -->
      <div>
        <label for="actor" class="block text-sm font-medium text-gray-700 mb-1">
          Actor
        </label>
        <select 
          id="actor" 
          v-model="selectedActor" 
          @change="updateFilters"
          class="filter-select"
        >
          <option value="">All Actors</option>
          <option v-for="actor in actors" :key="actor.id" :value="actor.id">
            {{ actor.name }}
          </option>
        </select>
      </div>

      <!-- Release Year Filter -->
      <div>
        <label for="year" class="block text-sm font-medium text-gray-700 mb-1">
          Release Year
        </label>
        <select 
          id="year" 
          v-model="selectedYear" 
          @change="updateFilters"
          class="filter-select"
        >
          <option value="">All Years</option>
          <option v-for="year in releaseYears" :key="year" :value="year">
            {{ year }}
          </option>
        </select>
      </div>
    </div>

    <div class="mt-4 flex justify-end">
      <button @click="clearFilters" class="btn-secondary">
        Clear Filters
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { Genre, Director, Actor, FilterOptions } from '@/types'

const props = defineProps<{
  genres: Genre[]
  directors: Director[]
  actors: Actor[]
  releaseYears: number[]
}>()

const emit = defineEmits<{
  filtersChanged: [filters: FilterOptions]
}>()

const selectedGenre = ref<number | string>('')
const selectedDirector = ref<number | string>('')
const selectedActor = ref<number | string>('')
const selectedYear = ref<number | string>('')

const updateFilters = () => {
  const filters: FilterOptions = {}
  
  if (selectedGenre.value) filters.genre_id = Number(selectedGenre.value)
  if (selectedDirector.value) filters.director_id = Number(selectedDirector.value)
  if (selectedActor.value) filters.actor_id = Number(selectedActor.value)
  if (selectedYear.value) filters.release_year = Number(selectedYear.value)
  
  emit('filtersChanged', filters)
}

const clearFilters = () => {
  selectedGenre.value = ''
  selectedDirector.value = ''
  selectedActor.value = ''
  selectedYear.value = ''
  emit('filtersChanged', {})
}
</script> 