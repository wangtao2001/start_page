module.exports = {
    pages: {
        index: {
            // index页面的入口
            entry: 'src/pages/index/main.js',
            // index页面模板来源
            template: 'public/index.html',
            // index页面最终打包在dist目录下输出文件名
            filename: 'index.html',
        },
        login: {
            // login页面的入口
            entry: 'src/pages/login/main.js',
            // login页面模板来源
            template: 'public/login.html',
            // login页面最终打包在dist目录下输出文件名
            filename: 'login.html'
        },
        space: {
            // space页面的入口
            entry: 'src/pages/space/main.js',
            // space页面模板来源
            template: 'public/space.html',
            // space页面最终打包在dist目录下输出文件名
            filename: 'space.html'
        },
        cloudnote: {
            // cloudnote页面的入口
            entry: 'src/pages/cloudnote/main.js',
            // cloudnote页面模板来源
            template: 'public/cloudnote.html',
            // cloudnote页面最终打包在dist目录下输出文件名
            filename: 'cloudnote.html'
        }
    }
}