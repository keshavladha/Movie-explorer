<template>
  <div>
    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-gray-600">Loading actor profile...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-md p-4">
      <div class="flex">
        <div class="ml-3">
          <h3 class="text-sm font-medium text-red-800">Error loading actor profile</h3>
          <div class="mt-2 text-sm text-red-700">
            <p>{{ error }}</p>
          </div>
          <div class="mt-4">
            <router-link to="/" class="btn-primary">
              Back to Movies
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Actor Profile -->
    <div v-else-if="actor" class="bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Header -->
      <div class="bg-gradient-to-r from-purple-600 to-indigo-600 text-white p-8">
        <div class="flex justify-between items-start">
          <div>
            <h1 class="text-4xl font-bold mb-2">{{ actor.name }}</h1>
            <p class="text-xl text-purple-100 mb-4" v-if="actor.birth_year">
              Born: {{ actor.birth_year }}
            </p>
          </div>
          <router-link to="/" class="btn-secondary">
            ← Back to Movies
          </router-link>
        </div>
      </div>

      <!-- Content -->
      <div class="p-8">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <!-- Biography -->
          <div class="lg:col-span-2">
            <div class="mb-8">
              <h2 class="text-2xl font-bold text-gray-900 mb-4">Biography</h2>
              <p class="text-gray-700 leading-relaxed">
                {{ actor.bio || 'No biography available for this actor.' }}
              </p>
            </div>
          </div>

          <!-- Stats -->
          <div class="lg:col-span-1">
            <div class="bg-gray-50 rounded-lg p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Career Stats</h3>
              <div class="space-y-3">
                <div>
                  <p class="text-sm text-gray-600">Movies Appeared In</p>
                  <p class="text-2xl font-bold text-gray-900">{{ actor.movies?.length || 0 }}</p>
                </div>
                <div v-if="actor.birth_year">
                  <p class="text-sm text-gray-600">Age</p>
                  <p class="text-2xl font-bold text-gray-900">{{ currentYear - actor.birth_year }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Filmography -->
        <div class="mt-12">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Filmography</h2>
          
          <div v-if="actor.movies && actor.movies.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <MovieCard 
              v-for="movie in actor.movies" 
              :key="movie.id" 
              :movie="movie" 
            />
          </div>
          
          <div v-else class="text-center py-12">
            <div class="text-gray-400 text-6xl mb-4">🎬</div>
            <h3 class="text-lg font-medium text-gray-900 mb-2">No movies found</h3>
            <p class="text-gray-600">This actor hasn't appeared in any movies in our database yet.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, computed } from 'vue'
import { useMovieStore } from '@/stores'
import MovieCard from '@/components/MovieCard.vue'
import type { Actor } from '@/types'

const props = defineProps<{
  id: string
}>()

const store = useMovieStore()
const actor = ref<Actor | null>(null)
const loading = ref(false)
const error = ref<string | null>(null)

const currentYear = computed(() => new Date().getFullYear())

const loadActor = async () => {
  const actorId = parseInt(props.id)
  if (isNaN(actorId)) {
    error.value = 'Invalid actor ID'
    return
  }

  loading.value = true
  error.value = null
  
  try {
    const actorData = await store.fetchActor(actorId)
    actor.value = actorData
  } catch (err) {
    error.value = 'Failed to load actor profile'
    console.error('Error loading actor:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadActor()
})

watch(() => props.id, () => {
  loadActor()
})
</script> 