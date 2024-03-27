--- Vue JS CDN ---
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

--- Vite JS ---
    npm create vite@latest 

    cd <your-project-name>
    npm install
    npm run dev

    npm run dev
    npm run build


--- Vue JS ---
    import { ... } from 'vue/dist/vue.esm-bundler.js'

    export default {
    data() { // data è una funzione che ritorna un oggetto
        return {
        message: 'Hello World!'
        }
    }
    }


-- v-bind ---
    <h1 v-bind:class="titleClass">Make me red</h1>
    <h1 :class="titleClass">Make me red</h1>

-- v-on ---
    <button v-on:click="increment">{{ count }}</button>
    <button @click="increment">{{ count }}</button>

-- v-model ---
    <input :value="text" @input="onInput" placeholder="Type here">
    <input v-model="text" placeholder="Type here">

-- v-if ---
    <h1 v-if="awesome">Vue is awesome!</h1>
    <h1 v-else>Oh no 😢</h1>

-- v-for & computed ---
    <script>
    let id = 0

    export default {
    data() {
        return {
        newTodo: '',
        hideCompleted: false,
        todos: [
            { id: id++, text: 'Learn HTML', done: true },
            { id: id++, text: 'Learn JavaScript', done: true },
            { id: id++, text: 'Learn Vue', done: false }
        ]
        }
    },
    computed: {
        filteredTodos() {
        return this.hideCompleted
            ? this.todos.filter((t) => !t.done)
            : this.todos
        }
    },
    methods: {
        addTodo() {
        this.todos.push({ id: id++, text: this.newTodo, done: false })
        this.newTodo = ''
        },
        removeTodo(todo) {
        this.todos = this.todos.filter((t) => t !== todo)
        }
    }
    </script>

    <template>
    <form @submit.prevent="addTodo">
        <input v-model="newTodo" required placeholder="new todo">
        <button>Add Todo</button>
    </form>
    <ul>
        <li v-for="todo in filteredTodos" :key="todo.id">
        <input type="checkbox" v-model="todo.done">
        <span :class="{ done: todo.done }">{{ todo.text }}</span>
        <button @click="removeTodo(todo)">X</button>
        </li>
    </ul>
    <button @click="hideCompleted = !hideCompleted">
        {{ hideCompleted ? 'Show all' : 'Hide completed' }}
    </button>
    </template>

    <style>
    .done {
    text-decoration: line-through;
    }
    </style>


--- Template Ref ---
    <script>
    export default {
        mounted() {
            this.$refs.pElementRef.textContent = 'mounted!'
        }
    }
    </script>

    <template>
        <p ref="pElementRef">hello</p>
    </template>


--- Watchers ---
    <script>
    export default {
    data() {
        return {
        todoId: 1,
        todoData: null
        }
    },
    methods: {
        async fetchData() {
        this.todoData = null
        const res = await fetch(
            `https://jsonplaceholder.typicode.com/todos/${this.todoId}`
        )
        this.todoData = await res.json()
        }
    },
    mounted() {
        this.fetchData()
    },
    watch: {
        todoId() {
        this.fetchData()
        }
    }
    }
    </script>

    <template>
    <p>Todo id: {{ todoId }}</p>
    <button @click="todoId++" :disabled="!todoData">Fetch next todo</button>
    <p v-if="!todoData">Loading...</p>
    <pre v-else>{{ todoData }}</pre>
    </template>


--- Import component ---
    <script>
    import ChildComp from './ChildComp.vue'

    export default {
    components: {
        ChildComp
    },
    data() {
        return {
        greeting: 'Hello from parent'
        }
    }
    }
    </script>

    <template>
    <ChildComp :msg="greeting"/>
    </template>


--- Emit ---
    <script>
    import ChildComp from './ChildComp.vue'

    export default {
    components: {
        ChildComp
    },
    data() {
        return {
        childMsg: 'No child msg yet'
        }
    }
    }
    </script>

    <template>
    <ChildComp @response="(msg) => childMsg = msg" />
    <p>{{ childMsg }}</p>
    </template>

    <script>
    export default {
    emits: ['response'],
    created() {
        this.$emit('response', 'hello from child')
    }
    }
    </script>

    <template>
    <h2>Child component</h2>
    </template>