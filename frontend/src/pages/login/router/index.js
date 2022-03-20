import VueRouter from "vue-router";
import login from "../../../views/login.vue"
import register from "../../../views/register.vue"

export default new VueRouter({
    mode: "history", // history模式
    // 在二级地址下面的 history mode 我不理解
    // hash mode 是 localhost:8080/login#/login ①
    // history mode 变 localhost:8080/login
    // 但其实这样反而更好
    // hash mode 下 localhost:8080/login 是啥都没有 必须重定向 到 localhost:8080/login#/login
    // history mode 下 localhost:8080/login 直接相当于 localhost:8080/login#/login ①
    routes: [
        {
            name: "login",
            path: '/login', 
            component : login        
        },
        {
            name: "register",
            path: '/register',
            component: register
        }
    ]
})