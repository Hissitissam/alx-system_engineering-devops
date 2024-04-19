#install the package puppet lint
package { 'puppet-lint':
  ensure   => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
